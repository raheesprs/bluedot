import re

with open('news.html', 'r') as f:
    content = f.read()

# Replace everything from FLEET BANNER to FOOTER
start_marker = "    <!-- ========== FLEET BANNER ========== -->"
end_marker = "    <!-- ========== FOOTER ========== -->"

if start_marker in content and end_marker in content:
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    new_html = """    <!-- ========== NEWS HERO SECTION ========== -->
    <section class="news-hero-section">
        <div class="news-hero-bg">
            <img src="images/news-1.png" alt="ITIJ Awards 2025" class="news-hero-img">
            <div class="news-hero-overlay"></div>
        </div>
        <div class="container h-100 position-relative z-1">
            <div class="news-hero-content">
                <p class="news-meta">Published on 18 Dec 2025 - 1.20 min read</p>
                <h1 class="news-title">Bluedot Wins Marketing Campaign of the Year at the<br>2025 ITIJ Awards</h1>
                <a href="#" class="btn-read-article">Read Article</a>
            </div>
        </div>
    </section>

"""
    
    content = content[:start_idx] + new_html + content[end_idx:]
    
    with open('news.html', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Markers not found")
