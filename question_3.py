import random

def digital_content_chatbot():
    """
    Comprehensive Digital Content Recommendation Chatbot
    Recommends movies, series, documentaries, and other digital content
    """
    
    print(" Welcome to ContentBot - Your Personal Digital Entertainment Assistant! ")
    print("=" * 80)
    
    # Get user's name
    name = input("What's your name? ").strip()
    if not name:
        name = "Friend"
    print(f"\nHello {name}! I'm here to help you discover amazing content to watch! ")
    
    # Initialize user preferences
    user_preferences = {}
    
    # Question 1: Content Type
    print("\n" + "=" * 50)
    print("QUESTION 1: What type of content are you in the mood for?")
    content_types = ['movie', 'tv series', 'documentary', 'anime', 'short film', 
                    'stand-up comedy', 'kids content', 'reality show', 'talk show', 
                    'cooking show', 'travel show', 'nature documentary', 'true crime']
    
    for i, content in enumerate(content_types, 1):
        print(f"{i}. {content.title()}")
    
    while True:
        try:
            choice = int(input(f"\nEnter your choice (1-{len(content_types)}): "))
            if 1 <= choice <= len(content_types):
                user_preferences['content_type'] = content_types[choice-1]
                break
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a number!")
    
    # Question 2: Genre
    print("\n" + "=" * 50)
    print("QUESTION 2: What genre appeals to you today?")
    genres = ['action', 'adventure', 'animation', 'biography', 'comedy', 'crime', 
              'drama', 'family', 'fantasy', 'horror', 'musical', 'mystery', 
              'romance', 'sci-fi', 'thriller', 'war', 'western', 'sports', 
              'historical', 'psychological', 'supernatural']
    
    for i, genre in enumerate(genres, 1):
        print(f"{i}. {genre.title()}")
    
    while True:
        try:
            choice = int(input(f"\nEnter your choice (1-{len(genres)}): "))
            if 1 <= choice <= len(genres):
                user_preferences['genre'] = genres[choice-1]
                break
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a number!")
    
    # Question 3: Mood
    print("\n" + "=" * 50)
    print("QUESTION 3: What's your current mood?")
    moods = ['happy and upbeat', 'sad and contemplative', 'adventurous', 
             'romantic', 'thrilled/excited', 'relaxed', 'curious/learning', 
             'nostalgic', 'energetic', 'thoughtful', 'escapist']
    
    for i, mood in enumerate(moods, 1):
        print(f"{i}. {mood.title()}")
    
    while True:
        try:
            choice = int(input(f"\nEnter your choice (1-{len(moods)}): "))
            if 1 <= choice <= len(moods):
                user_preferences['mood'] = moods[choice-1]
                break
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a number!")
    
    # Question 4: Time Available
    print("\n" + "=" * 50)
    print("QUESTION 4: How much time do you have?")
    time_options = ['under 30 minutes', '30-60 minutes', '1-2 hours', 
                   '2-3 hours', '3+ hours', 'binge-watching session']
    
    for i, time_opt in enumerate(time_options, 1):
        print(f"{i}. {time_opt.title()}")
    
    while True:
        try:
            choice = int(input(f"\nEnter your choice (1-{len(time_options)}): "))
            if 1 <= choice <= len(time_options):
                user_preferences['time_available'] = time_options[choice-1]
                break
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a number!")
    
    # Question 5: Age Rating
    print("\n" + "=" * 50)
    print("QUESTION 5: What age rating are you comfortable with?")
    age_ratings = ['G (General)', 'PG (Parental Guidance)', 'PG-13 (Teen)', 
                  'R (Mature)', 'NC-17 (Adult)', 'TV-Y (Kids)', 'TV-14 (Teen TV)', 
                  'TV-MA (Mature TV)', 'no preference']
    
    for i, rating in enumerate(age_ratings, 1):
        print(f"{i}. {rating}")
    
    while True:
        try:
            choice = int(input(f"\nEnter your choice (1-{len(age_ratings)}): "))
            if 1 <= choice <= len(age_ratings):
                user_preferences['age_rating'] = age_ratings[choice-1]
                break
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a number!")
    
    # Question 6: Language Preference
    print("\n" + "=" * 50)
    print("QUESTION 6: What language do you prefer?")
    languages = ['english', 'spanish', 'french', 'german', 'italian', 'japanese', 
                'korean', 'chinese', 'hindi', 'arabic', 'portuguese', 'russian', 
                'subtitled foreign films', 'no preference']
    
    for i, lang in enumerate(languages, 1):
        print(f"{i}. {lang.title()}")
    
    while True:
        try:
            choice = int(input(f"\nEnter your choice (1-{len(languages)}): "))
            if 1 <= choice <= len(languages):
                user_preferences['language'] = languages[choice-1]
                break
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a number!")
    
    # Question 7: Streaming Platform
    print("\n" + "=" * 50)
    print("QUESTION 7: Which streaming platforms do you have access to?")
    platforms = ['netflix', 'amazon prime video', 'disney+', 'hbo max', 'hulu', 
                'apple tv+', 'paramount+', 'peacock', 'youtube premium', 
                'crunchyroll', 'funimation', 'free platforms', 'any platform']
    
    selected_platforms = []
    print("(You can select multiple platforms. Type 'done' when finished)")
    
    for i, platform in enumerate(platforms, 1):
        print(f"{i}. {platform.title()}")
    
    while True:
        user_input = input(f"\nEnter platform number (1-{len(platforms)}) or 'done': ").strip().lower()
        if user_input == 'done':
            if selected_platforms:
                break
            else:
                print("Please select at least one platform!")
                continue
        
        try:
            choice = int(user_input)
            if 1 <= choice <= len(platforms):
                platform = platforms[choice-1]
                if platform not in selected_platforms:
                    selected_platforms.append(platform)
                    print(f"Added: {platform.title()}")
                else:
                    print("Platform already selected!")
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a number or 'done'!")
    
    user_preferences['platforms'] = selected_platforms
    
    # Question 8: New vs Old Content
    print("\n" + "=" * 50)
    print("QUESTION 8: Do you prefer newer or older content?")
    content_age = ['brand new (2024-2026)', 'recent (2020-2023)', 'modern (2010-2019)', 
                  'classic (2000-2009)', 'vintage (1990s)', 'retro (1980s or older)', 'no preference']
    
    for i, age in enumerate(content_age, 1):
        print(f"{i}. {age.title()}")
    
    while True:
        try:
            choice = int(input(f"\nEnter your choice (1-{len(content_age)}): "))
            if 1 <= choice <= len(content_age):
                user_preferences['content_age'] = content_age[choice-1]
                break
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a number!")
    
    # Question 9: Popularity
    print("\n" + "=" * 50)
    print("QUESTION 9: Do you prefer popular hits or hidden gems?")
    popularity = ['mainstream blockbusters', 'popular but not too mainstream', 
                 'critically acclaimed', 'hidden gems', 'cult classics', 'no preference']
    
    for i, pop in enumerate(popularity, 1):
        print(f"{i}. {pop.title()}")
    
    while True:
        try:
            choice = int(input(f"\nEnter your choice (1-{len(popularity)}): "))
            if 1 <= choice <= len(popularity):
                user_preferences['popularity'] = popularity[choice-1]
                break
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a number!")
    
    # Question 10: Emotional Intensity
    print("\n" + "=" * 50)
    print("QUESTION 10: What emotional intensity do you want?")
    intensity = ['light and fun', 'moderate emotions', 'emotionally intense', 
                'heart-wrenching', 'mind-bending', 'adrenaline-pumping', 'peaceful and calming']
    
    for i, intense in enumerate(intensity, 1):
        print(f"{i}. {intense.title()}")
    
    while True:
        try:
            choice = int(input(f"\nEnter your choice (1-{len(intensity)}): "))
            if 1 <= choice <= len(intensity):
                user_preferences['intensity'] = intensity[choice-1]
                break
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a number!")
    
    # Question 11: Watching Company
    print("\n" + "=" * 50)
    print("QUESTION 11: Who will you be watching with?")
    company = ['alone', 'romantic partner', 'family with kids', 'friends', 
              'family (adults only)', 'large group', 'varies']
    
    for i, comp in enumerate(company, 1):
        print(f"{i}. {comp.title()}")
    
    while True:
        try:
            choice = int(input(f"\nEnter your choice (1-{len(company)}): "))
            if 1 <= choice <= len(company):
                user_preferences['company'] = company[choice-1]
                break
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a number!")
    
    # Question 12: Setting/Environment
    print("\n" + "=" * 50)
    print("QUESTION 12: What kind of setting interests you?")
    settings = ['modern urban', 'historical period', 'futuristic', 'fantasy world', 
               'small town', 'wilderness/nature', 'space', 'underwater', 
               'different country/culture', 'post-apocalyptic', 'magical realm', 'no preference']
    
    for i, setting in enumerate(settings, 1):
        print(f"{i}. {setting.title()}")
    
    while True:
        try:
            choice = int(input(f"\nEnter your choice (1-{len(settings)}): "))
            if 1 <= choice <= len(settings):
                user_preferences['setting'] = settings[choice-1]
                break
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a number!")
    
    # Question 13: Favorite Actors/Directors
    print("\n" + "=" * 50)
    print("QUESTION 13: Do you have any favorite actors or directors? (Optional)")
    favorites = input("Enter names separated by commas (or press Enter to skip): ").strip()
    user_preferences['favorites'] = favorites if favorites else "none specified"
    
    # Question 14: Content to Avoid
    print("\n" + "=" * 50)
    print("QUESTION 14: Any content you want to avoid?")
    avoid_content = ['violence', 'horror/scary', 'sad endings', 'explicit content', 
                    'slow paced', 'subtitles', 'black and white', 'musicals', 
                    'very long content', 'cliffhangers', 'nothing to avoid']
    
    selected_avoid = []
    print("(You can select multiple options. Type 'done' when finished)")
    
    for i, avoid in enumerate(avoid_content, 1):
        print(f"{i}. {avoid.title()}")
    
    while True:
        user_input = input(f"\nEnter number (1-{len(avoid_content)}) or 'done': ").strip().lower()
        if user_input == 'done':
            break
        
        try:
            choice = int(user_input)
            if 1 <= choice <= len(avoid_content):
                avoid = avoid_content[choice-1]
                if avoid not in selected_avoid:
                    selected_avoid.append(avoid)
                    print(f"Added to avoid: {avoid.title()}")
                else:
                    print("Already selected!")
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a number or 'done'!")
    
    user_preferences['avoid'] = selected_avoid if selected_avoid else ["nothing to avoid"]
    
    # Question 15: Specific Requests
    print("\n" + "=" * 50)
    print("QUESTION 15: Any specific themes or topics you're interested in? (Optional)")
    specific_interest = input("Describe what you're looking for: ").strip()
    user_preferences['specific_interest'] = specific_interest if specific_interest else "none specified"
    
    return user_preferences


def create_content_database():
    """
    Creates a comprehensive database of digital content with various attributes
    """
    return [
        # Movies
        {"title": "The Shawshank Redemption", "type": "movie", "genre": "drama", "year": 1994, 
         "rating": "R", "platform": "netflix", "mood": "contemplative", "setting": "prison"},
        {"title": "Inception", "type": "movie", "genre": "sci-fi", "year": 2010, 
         "rating": "PG-13", "platform": "hbo max", "mood": "thrilled", "setting": "futuristic"},
        {"title": "The Princess Bride", "type": "movie", "genre": "adventure", "year": 1987, 
         "rating": "PG", "platform": "disney+", "mood": "happy", "setting": "fantasy world"},
        {"title": "Pulp Fiction", "type": "movie", "genre": "crime", "year": 1994, 
         "rating": "R", "platform": "netflix", "mood": "energetic", "setting": "modern urban"},
        {"title": "Spirited Away", "type": "movie", "genre": "animation", "year": 2001, 
         "rating": "PG", "platform": "hbo max", "mood": "adventurous", "setting": "magical realm"},
        {"title": "The Grand Budapest Hotel", "type": "movie", "genre": "comedy", "year": 2014, 
         "rating": "R", "platform": "disney+", "mood": "happy", "setting": "historical period"},
        {"title": "Mad Max: Fury Road", "type": "movie", "genre": "action", "year": 2015, 
         "rating": "R", "platform": "hbo max", "mood": "adrenaline-pumping", "setting": "post-apocalyptic"},
        {"title": "Her", "type": "movie", "genre": "romance", "year": 2013, 
         "rating": "R", "platform": "netflix", "mood": "contemplative", "setting": "futuristic"},
        {"title": "Finding Nemo", "type": "movie", "genre": "family", "year": 2003, 
         "rating": "G", "platform": "disney+", "mood": "happy", "setting": "underwater"},
        {"title": "The Godfather", "type": "movie", "genre": "crime", "year": 1972, 
         "rating": "R", "platform": "paramount+", "mood": "thoughtful", "setting": "historical period"},
        
        # TV Series
        {"title": "Breaking Bad", "type": "tv series", "genre": "drama", "year": 2008, 
         "rating": "TV-MA", "platform": "netflix", "mood": "intense", "setting": "modern urban"},
        {"title": "The Office", "type": "tv series", "genre": "comedy", "year": 2005, 
         "rating": "TV-14", "platform": "peacock", "mood": "happy", "setting": "modern urban"},
        {"title": "Stranger Things", "type": "tv series", "genre": "sci-fi", "year": 2016, 
         "rating": "TV-14", "platform": "netflix", "mood": "thrilled", "setting": "small town"},
        {"title": "The Mandalorian", "type": "tv series", "genre": "sci-fi", "year": 2019, 
         "rating": "TV-14", "platform": "disney+", "mood": "adventurous", "setting": "space"},
        {"title": "Friends", "type": "tv series", "genre": "comedy", "year": 1994, 
         "rating": "TV-14", "platform": "hbo max", "mood": "happy", "setting": "modern urban"},
        {"title": "Game of Thrones", "type": "tv series", "genre": "fantasy", "year": 2011, 
         "rating": "TV-MA", "platform": "hbo max", "mood": "intense", "setting": "fantasy world"},
        {"title": "The Crown", "type": "tv series", "genre": "drama", "year": 2016, 
         "rating": "TV-MA", "platform": "netflix", "mood": "thoughtful", "setting": "historical period"},
        {"title": "Rick and Morty", "type": "tv series", "genre": "animation", "year": 2013, 
         "rating": "TV-14", "platform": "hulu", "mood": "energetic", "setting": "space"},
        {"title": "Euphoria", "type": "tv series", "genre": "drama", "year": 2019, 
         "rating": "TV-MA", "platform": "hbo max", "mood": "intense", "setting": "modern urban"},
        {"title": "Ted Lasso", "type": "tv series", "genre": "comedy", "year": 2020, 
         "rating": "TV-MA", "platform": "apple tv+", "mood": "uplifting", "setting": "small town"},
        
        # Documentaries
        {"title": "Planet Earth", "type": "documentary", "genre": "nature documentary", "year": 2006, 
         "rating": "TV-G", "platform": "netflix", "mood": "peaceful", "setting": "nature"},
        {"title": "Making a Murderer", "type": "documentary", "genre": "true crime", "year": 2015, 
         "rating": "TV-MA", "platform": "netflix", "mood": "contemplative", "setting": "modern urban"},
        {"title": "Free Solo", "type": "documentary", "genre": "sports", "year": 2018, 
         "rating": "PG-13", "platform": "disney+", "mood": "adrenaline-pumping", "setting": "nature"},
        {"title": "Won't You Be My Neighbor?", "type": "documentary", "genre": "biography", "year": 2018, 
         "rating": "PG-13", "platform": "hbo max", "mood": "uplifting", "setting": "modern urban"},
        {"title": "The Social Dilemma", "type": "documentary", "genre": "technology", "year": 2020, 
         "rating": "PG-13", "platform": "netflix", "mood": "thoughtful", "setting": "modern urban"},
        
        # Anime
        {"title": "Attack on Titan", "type": "anime", "genre": "action", "year": 2013, 
         "rating": "TV-MA", "platform": "crunchyroll", "mood": "intense", "setting": "fantasy world"},
        {"title": "My Hero Academia", "type": "anime", "genre": "adventure", "year": 2016, 
         "rating": "TV-14", "platform": "crunchyroll", "mood": "energetic", "setting": "modern urban"},
        {"title": "Demon Slayer", "type": "anime", "genre": "action", "year": 2019, 
         "rating": "TV-14", "platform": "crunchyroll", "mood": "intense", "setting": "historical period"},
        {"title": "One Piece", "type": "anime", "genre": "adventure", "year": 1999, 
         "rating": "TV-14", "platform": "crunchyroll", "mood": "adventurous", "setting": "fantasy world"},
        
        # Comedy Specials
        {"title": "Dave Chappelle: Sticks & Stones", "type": "stand-up comedy", "genre": "comedy", "year": 2019, 
         "rating": "TV-MA", "platform": "netflix", "mood": "energetic", "setting": "modern urban"},
        {"title": "John Mulaney: Kid Gorgeous", "type": "stand-up comedy", "genre": "comedy", "year": 2018, 
         "rating": "TV-14", "platform": "netflix", "mood": "happy", "setting": "modern urban"},
        
        # Reality Shows
        {"title": "The Great British Bake Off", "type": "reality show", "genre": "cooking show", "year": 2010, 
         "rating": "TV-G", "platform": "netflix", "mood": "peaceful", "setting": "modern urban"},
        {"title": "Queer Eye", "type": "reality show", "genre": "lifestyle", "year": 2018, 
         "rating": "TV-14", "platform": "netflix", "mood": "uplifting", "setting": "modern urban"},
        
        # Kids Content
        {"title": "Avatar: The Last Airbender", "type": "kids content", "genre": "adventure", "year": 2005, 
         "rating": "TV-Y7", "platform": "netflix", "mood": "adventurous", "setting": "fantasy world"},
        {"title": "Steven Universe", "type": "kids content", "genre": "animation", "year": 2013, 
         "rating": "TV-PG", "platform": "hbo max", "mood": "uplifting", "setting": "modern urban"},
        
        # Short Films
        {"title": "Paperman", "type": "short film", "genre": "animation", "year": 2012, 
         "rating": "G", "platform": "disney+", "mood": "romantic", "setting": "modern urban"},
        {"title": "The Present", "type": "short film", "genre": "drama", "year": 2014, 
         "rating": "PG", "platform": "youtube premium", "mood": "contemplative", "setting": "modern urban"}
    ]


def generate_recommendations(user_preferences, content_database):
    """
    Generate personalized recommendations based on user preferences
    """
    recommendations = []
    
    # Score each content item based on user preferences
    for content in content_database:
        score = 0
        reasons = []
        
        # Match content type
        if content["type"] == user_preferences["content_type"]:
            score += 10
            reasons.append(f"matches your preferred content type ({user_preferences['content_type']})")
        
        # Match genre
        if content["genre"] == user_preferences["genre"]:
            score += 8
            reasons.append(f"matches your preferred genre ({user_preferences['genre']})")
        
        # Match platform availability
        content_platform = content["platform"].lower()
        user_platforms = [p.lower() for p in user_preferences["platforms"]]
        if content_platform in user_platforms or "any platform" in user_platforms:
            score += 6
            reasons.append(f"available on {content['platform']}")
        
        # Match mood/setting
        if "mood" in content and content["mood"] in user_preferences["mood"]:
            score += 5
            reasons.append(f"matches your current mood")
        
        if "setting" in content and content["setting"] in user_preferences["setting"]:
            score += 4
            reasons.append(f"set in {content['setting']}")
        
        # Age preference matching
        content_year = content.get("year", 2000)
        if "brand new" in user_preferences["content_age"] and content_year >= 2024:
            score += 3
        elif "recent" in user_preferences["content_age"] and 2020 <= content_year <= 2023:
            score += 3
        elif "modern" in user_preferences["content_age"] and 2010 <= content_year <= 2019:
            score += 3
        elif "classic" in user_preferences["content_age"] and 2000 <= content_year <= 2009:
            score += 3
        elif "vintage" in user_preferences["content_age"] and 1990 <= content_year <= 1999:
            score += 3
        elif "retro" in user_preferences["content_age"] and content_year < 1990:
            score += 3
        
        # Random bonus for variety
        score += random.randint(0, 3)
        
        if score > 5:  # Only include items with reasonable relevance
            recommendations.append({
                "content": content,
                "score": score,
                "reasons": reasons
            })
    
    # Sort by score and return top recommendations
    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return recommendations[:10]  # Return top 10 recommendations


def display_recommendations(recommendations, user_name):
    """
    Display the recommendations in a user-friendly format
    """
    print("\n" + "=" * 25)
    print(f" PERSONALIZED RECOMMENDATIONS FOR {user_name.upper()} ")
    print("=" * 25)
    
    if not recommendations:
        print("I'm sorry, I couldn't find any content matching your preferences.")
        print("You might want to try adjusting some of your criteria!")
        return
    
    for i, rec in enumerate(recommendations[:5], 1):
        content = rec["content"]
        print(f"\n#{i}  {content['title']}")
        print(f"    Type: {content['type'].title()}")
        print(f"    Genre: {content['genre'].title()}")
        print(f"    Year: {content['year']}")
        print(f"    Rating: {content['rating']}")
        print(f"    Platform: {content['platform'].title()}")
        print(f"    Match Score: {rec['score']}/25")
        if rec["reasons"]:
            print(f"    Why this recommendation: {', '.join(rec['reasons'])}.")
        print("-" * 60)
    
    print(f"\n Based on your preferences, I found {len(recommendations)} great options!")
    print("Enjoy your viewing experience! ")


def run_chatbot():
    """
    Main function to run the digital content chatbot
    """
    try:
        # Collect user preferences
        preferences = digital_content_chatbot()
        
        # Create content database
        content_db = create_content_database()
        
        # Generate recommendations
        recommendations = generate_recommendations(preferences, content_db)
        
        # Display results
        user_name = preferences.get('name', 'Friend')
        display_recommendations(recommendations, user_name)
        
        # Ask if user wants to see more details
        print("\n" + "=" * 60)
        show_more = input("Would you like to see your complete preference profile? (y/n): ").lower()
        
        if show_more == 'y':
            print("\n📋 YOUR PREFERENCE PROFILE:")
            print("=" * 40)
            for key, value in preferences.items():
                if isinstance(value, list):
                    value = ", ".join(value)
                print(f"{key.replace('_', ' ').title()}: {value}")
        
        print(f"\nThank you for using ContentBot! Happy watching! ")
        
    except KeyboardInterrupt:
        print("\n\nThanks for using ContentBot! Come back anytime! ")
    except Exception as e:
        print(f"\nOops! Something went wrong: {e}")
        print("Please try running the chatbot again!")


if __name__ == "__main__":
    run_chatbot()