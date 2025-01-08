from flask import Flask, render_template, jsonify

app = Flask(__name__)

CATEGORIES = [{
    "id": 1,
    "name": "World"
}, {
    "id": 2,
    "name": "Business"
}, {
    "id": 3,
    "name": "Technology"
}, {
    "id": 4,
    "name": "Entertainment"
}, {
    "id": 5,
    "name": "Sports"
}]

NEWS = [
    {
        'id': 1,
        'title': 'Earthquake of 7.1 magnitude hits Tibet',
        'description':
        'A 7.1 magnitude earthquake hit Tibet in August, causing widespread devastation across the region. Thousands of buildings were destroyed, and entire communities were affected. Emergency services have been deployed, and international aid has started arriving. The death toll is expected to rise as search-and-rescue operations continue, and authorities are urging people to remain vigilant for aftershocks.',
        'author': 'Jane Doe',
        'published_date': "1/8/2025",
        'category_id': 1,
        'image_url': 'https://example.com/images/earthquake-tibet.jpg'
    },
    {
        'id': 2,
        'title': 'Global warming raises sea levels by 2 inches',
        'description':
        'Recent studies have revealed that global warming has contributed to a 2-inch rise in sea levels over the past decade. This increase has caused significant flooding in coastal areas, affecting millions of people. Experts warn that without substantial reductions in greenhouse gas emissions, sea levels could continue to rise, leading to more devastating consequences for vulnerable populations and ecosystems worldwide.',
        'author': 'John Smith',
        'published_date': "1/7/2025",
        'category_id': 1,
        'image_url': 'https://example.com/images/global-warming-sea-level.jpg'
    },
    {
        'id': 3,
        'title': 'New species of butterfly discovered in the Amazon',
        'description':
        'A team of scientists has discovered a previously unknown species of butterfly in the heart of the Amazon rainforest. The butterfly, which has vibrant, iridescent wings, was spotted during an expedition to study biodiversity in one of the world’s most ecologically rich areas. This discovery highlights the critical importance of conserving natural habitats in the face of deforestation and climate change, as new species are still being uncovered in these untouched regions.',
        'author': 'Emily Taylor',
        'published_date': "1/6/2025",
        'category_id': 3,
        'image_url': 'https://example.com/images/amazon-butterfly.jpg'
    },
    {
        'id': 4,
        'title': 'Stock markets hit an all-time high',
        'description':
        'The global stock markets have reached an all-time high, with major indexes breaking previous records due to strong economic growth and investor optimism. Analysts attribute the surge to a combination of factors, including a boom in tech stocks, renewed consumer spending, and a stable geopolitical climate. However, experts caution that the markets remain vulnerable to potential corrections and that investors should stay alert to any signals of a downturn.',
        'author': 'Michael Brown',
        'published_date': "1/5/2025",
        'category_id': 2,
        'image_url': 'https://example.com/images/stock-market-high.jpg'
    },
    {
        'id': 5,
        'title': 'SpaceX launches new satellite into orbit',
        'description':
        'SpaceX successfully launched a new satellite into orbit last week, further expanding the reach of global internet coverage. This satellite is part of the company’s Starlink project, which aims to provide high-speed internet to underserved and remote areas worldwide. The successful launch marks another milestone in SpaceX’s ongoing efforts to revolutionize space travel and connectivity, with ambitious plans to launch even more satellites in the coming years.',
        'author': 'Sarah Johnson',
        'published_date': "1/4/2025",
        'category_id': 3,
        'image_url': 'https://example.com/images/spacex-satellite.jpg'
    },
    {
        'id': 6,
        'title': 'AI technology transforms the healthcare industry',
        'description':
        'Artificial Intelligence (AI) is increasingly becoming a transformative force in healthcare. From improving diagnostic accuracy to enhancing personalized treatment plans, AI technology is revolutionizing the way medical professionals provide care. A recent report showed that AI-powered diagnostic tools are now able to detect certain diseases with greater precision than human doctors. This technological breakthrough is expected to improve patient outcomes, streamline medical processes, and reduce healthcare costs globally.',
        'author': 'David Wilson',
        'published_date': "1/3/2025",
        'category_id': 3,
        'image_url': 'https://example.com/images/ai-healthcare.jpg'
    },
    {
        'id': 7,
        'title': 'Electric vehicles dominate the auto market',
        'description':
        'Electric vehicles (EVs) have rapidly gained market share, outselling traditional gas-powered cars in several major markets. Advances in battery technology, combined with growing environmental awareness, have made EVs more affordable and practical for consumers. Governments around the world are also supporting the transition to electric mobility with incentives and infrastructure investments. This shift is expected to lead to a significant decrease in carbon emissions from the transportation sector, further accelerating the move towards sustainability.',
        'author': 'Laura Green',
        'published_date': "1/2/2025",
        'category_id': 3,
        'image_url': 'https://example.com/images/electric-vehicles.jpg'
    },
    {
        'id': 8,
        'title': 'Olympics 2024 breaks records in attendance',
        'description':
        'The 2024 Summer Olympics in Paris has broken records for attendance, with millions of spectators from all over the world coming to support their athletes. The event has also seen record viewership on digital platforms, with live streaming drawing an unprecedented global audience. The opening ceremony, featuring a spectacular mix of culture and technology, set the tone for what is expected to be one of the most successful Olympics in modern history.',
        'author': 'James White',
        'published_date': "1/1/2025",
        'category_id': 4,
        'image_url': 'https://example.com/images/olympics-2024.jpg'
    },
    {
        'id': 9,
        'title': 'New movie set to break box office records',
        'description':
        'A new action-packed blockbuster movie is expected to break box office records during its opening weekend. Early reviews suggest that the film, which features groundbreaking special effects and a star-studded cast, will be a major hit with audiences around the world. The movie’s director has also been praised for pushing the boundaries of cinematic technology, creating an experience that is both visually stunning and emotionally gripping.',
        'author': 'Olivia Martin',
        'published_date': "12/31/2024",
        'category_id': 4,
        'image_url': 'https://example.com/images/new-blockbuster.jpg'
    },
    {
        'id': 10,
        'title': 'Football championship reaches new heights of excitement',
        'description':
        'The national football championship this year has reached new heights in terms of excitement and competition. The final match between the top two teams was a nail-biting spectacle, drawing millions of fans from across the country. Both teams showed incredible skill and teamwork, with the game ultimately being decided in the final moments. Fans are already calling it one of the best championship games in recent memory.',
        'author': 'Liam King',
        'published_date': "12/30/2024",
        'category_id': 5,
        'image_url': 'https://example.com/images/football-championship.jpg'
    },
    {
        'id': 11,
        'title': 'Cristiano Ronaldo announces retirement from football',
        'description':
        'In a heartfelt message to his fans, football superstar Cristiano Ronaldo announced his retirement from professional football at the age of 40. Ronaldo, who has won numerous titles and set countless records, thanked his fans, family, and teammates for their support over the years. He expressed his pride in his career and hinted at future ventures, including a possible role in coaching or sports entrepreneurship.',
        'author': 'Sophia Lee',
        'published_date': "12/29/2024",
        'category_id': 5,
        'image_url': 'https://example.com/images/ronaldo-retirement.jpg'
    },
    {
        'id': 12,
        'title': 'Formula 1 launches a new electric car racing series',
        'description':
        'Formula 1 has announced a new electric car racing series, marking the sport’s commitment to sustainability and cutting-edge technology. The series will feature fully electric vehicles racing on custom-designed tracks, with the aim of showcasing the performance of green energy vehicles in a high-speed competitive setting. Fans of the sport are excited about the new series, which is expected to bring innovation and excitement to the world of motorsport.',
        'author': 'Daniel Carter',
        'published_date': "12/28/2024",
        'category_id': 5,
        'image_url': 'https://example.com/images/formula1-electric.jpg'
    },
]


@app.route("/")
def hello_world():
    return render_template('home.html', categories=CATEGORIES, news=NEWS)


@app.route("/api/news")
def list_news():
    return jsonify(NEWS)


@app.route("/api/categories")
def list_categories():
    return jsonify(CATEGORIES)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
