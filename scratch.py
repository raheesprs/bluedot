import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

insert_block = """
                        <!-- Mobile Nav Actions -->
                        <div class="mobile-nav-actions d-md-none mt-5">
                            <div class="d-flex flex-column align-items-start gap-3">
                                <a href="tel:+971551881441" class="nav-outline-btn en-content"> <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"> <path d="M9.50246 4.25722C9.19873 3.4979 8.46332 3 7.64551 3H4.89474C3.8483 3 3 3.8481 3 4.89453C3 13.7892 10.2108 21 19.1055 21C20.1519 21 21 20.1516 21 19.1052L21.0005 16.354C21.0005 15.5361 20.5027 14.8009 19.7434 14.4971L17.1069 13.4429C16.4249 13.1701 15.6483 13.2929 15.0839 13.7632L14.4035 14.3307C13.6089 14.9929 12.4396 14.9402 11.7082 14.2088L9.79222 12.2911C9.06079 11.5596 9.00673 10.3913 9.66895 9.59668L10.2363 8.9163C10.7066 8.35195 10.8305 7.57516 10.5577 6.89309L9.50246 4.25722Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/> </svg> 24/7 Global Assistance</a>
                                <a href="tel:+971551881441" class="nav-outline-btn ar-content">المساعدة العالمية على مدار 24/7</a>
                                <a href="javascript:void(0)" class="nav-outline-btn trigger-enquiry en-content"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"> <path d="M5.59961 19.9203L7.12357 18.7012L7.13478 18.6926C7.45249 18.4384 7.61281 18.3101 7.79168 18.2188C7.95216 18.1368 8.12328 18.0771 8.2998 18.0408C8.49877 18 8.70603 18 9.12207 18H17.8031C18.921 18 19.4806 18 19.908 17.7822C20.2843 17.5905 20.5905 17.2842 20.7822 16.9079C21 16.4805 21 15.9215 21 14.8036V7.19691C21 6.07899 21 5.5192 20.7822 5.0918C20.5905 4.71547 20.2837 4.40973 19.9074 4.21799C19.4796 4 18.9203 4 17.8002 4H6.2002C5.08009 4 4.51962 4 4.0918 4.21799C3.71547 4.40973 3.40973 4.71547 3.21799 5.0918C3 5.51962 3 6.08009 3 7.2002V18.6712C3 19.7369 3 20.2696 3.21846 20.5433C3.40845 20.7813 3.69644 20.9198 4.00098 20.9195C4.35115 20.9191 4.76744 20.5861 5.59961 19.9203Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/> </svg> Make an Enquiry</a>
                                <a href="javascript:void(0)" class="nav-outline-btn trigger-enquiry ar-content">تقديم استفسار</a>
                                <div class="nav-lang mt-2">
                                    <span class="lang-current-label">EN</span>
                                    <i class="fas fa-chevron-down"></i>
                                    <div class="lang-dropdown">
                                        <span class="lang-option active" data-lang="en">
                                            <span class="lang-flag"></span>
                                            <span class="lang-name">EN</span>
                                        </span>
                                        <span class="lang-option" data-lang="ar">
                                            <span class="lang-flag"></span>
                                            <span class="lang-name">AR</span>
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
"""

success = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "<!-- Mobile Nav Actions -->" in content:
        continue
    
    # We look for the end of the ar-content ul and the closing div of nav-menu-main
    pattern = r'(</ul>\s*</div>\s*<!-- Services Submenu -->)'
    
    # Since whitespace can vary, we might want to just replace the div before the submenu
    if '<!-- Services Submenu -->' in content:
        # split at <!-- Services Submenu -->
        parts = content.split('<!-- Services Submenu -->')
        if len(parts) == 2:
            # find the last </div> before <!-- Services Submenu -->
            last_div_idx = parts[0].rfind('</div>')
            if last_div_idx != -1:
                new_part_0 = parts[0][:last_div_idx] + insert_block + parts[0][last_div_idx:]
                new_content = new_part_0 + '<!-- Services Submenu -->' + parts[1]
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                success += 1

print(f"Updated {success} files.")
