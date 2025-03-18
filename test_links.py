import re
import requests
import sys
from typing import Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed

thread_num = 20
check_timeout = 7


def extract_links_from_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Markdown link pattern: [text](URL)
    link_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\s)]+)\)')
    return [(match[0], match[1]) for match in link_pattern.findall(content)]


def check_link(link_text_pair) -> Tuple[str, str, int]:
    text, link = link_text_pair

    res = None
    try:
        response = requests.head(link, allow_redirects=True, timeout=check_timeout)
        res = link, text, response.status_code
    except requests.RequestException as e:
        res = link, text, -1
    
    print(f"[{res[2]}] [{text}] {link}")
    return res


def check_links(links, max_threads=thread_num):
    broken_links = []
    with ThreadPoolExecutor(max_threads) as executor:
        future_to_link = {executor.submit(check_link, link_text_pair): link_text_pair for link_text_pair in links}
        for future in as_completed(future_to_link):
            result = future.result()
            if result[2] != 200:
                broken_links.append(result)
    return broken_links


if __name__ == "__main__":
    markdown_file = "README.md"
    links = extract_links_from_markdown(markdown_file)
    
    if not links:
        print("No links found.")
        sys.exit(1)

    broken_links = check_links(links, max_threads=10)
    if broken_links:
        print("Broken Links:")
        for link, text, status in broken_links:
            print(f"[{status}] [{text}] {link}")
        sys.exit(1)

