import re
import requests

def replace_links(file_path, content, is_markdown=True):
    broken_links = []
    
    if is_markdown:
        pattern = r'\[(.*?)\]\((.*?)\)'
        
        def markdown_link_replacer(match):
            text = match.group(1)
            link = match.group(2)
            
            if not is_valid_link(link):
                broken_links.append(link)
                return f'<a href="#" style="color:red;">{text}</a>'
            
            return f'<a href="{link}">{text}</a>'
        
        updated_content = re.sub(pattern, markdown_link_replacer, content)
    else:
        url_pattern = r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)'
        
        def txt_link_replacer(match):
            url = match.group(1)
            
            if not is_valid_link(url):
                broken_links.append(url)
                return f'<a href="#" style="color:red;">{url}</a>'
            
            return f'<a href="{url}">{url}</a>'
        
        updated_content = re.sub(url_pattern, txt_link_replacer, content)
    
    return updated_content, broken_links

def is_valid_link(link):
    try:
        response = requests.head(link, allow_redirects=True, timeout=5)
        return response.status_code in [200, 301, 302]
    except requests.RequestException:
        return False
