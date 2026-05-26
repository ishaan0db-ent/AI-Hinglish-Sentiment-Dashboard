themes = {
    "Technology":[
        "phone","laptop","battery","charger","camera",
        "headphones","smartwatch","tablet","printer","router",
        "monitor","keyboard","mouse","speaker","microphone",
        "bug","software","hardware","gadget","device",
        "screen","app","game","virtual","augmented",
        "artificial","intelligence","machine","learning","data",
        "cloud","network","security","encryption","algorithm",
        "code","program","developer","engineer","hacker",
        "ui","ux","interface","user","experience","design",
        "fps","gpu","cpu","ram","storage",
    ],
    "Entertainment":[
        "movie","music","game","tv","show",
        "actor","actress","director","producer","studio",
        "concert","festival","album","song","band",
        "comedy","drama","action","adventure","horror",
        "romance","sci-fi","fantasy","animation","documentary",
        "theater","performance","art","exhibition","gallery",
        "celebrity","famous","star","award","red carpet",
        "film","netflix", "anime"
    ],
    "Sports":[
        "football","soccer","basketball","baseball","tennis",
        "golf","hockey","swimming","running","cycling",
        "athlete","team","coach","league","tournament",
        "championship","medal","olympics","world cup",
        "score","goal","win","lose","draw",
        "referee","stadium","fan","supporter","rivalry",
        "training", "fitness", "exercise", "workout", "gym",
        "cricket","rugby","boxing","mma","wrestling",
        "olympic","marathon","triathlon","surfing","skateboarding",

    ],
    "Telecom":[
        "phone","mobile","cellular","network","signal",
        "tower","antenna","coverage","data","roaming",
        "sms","mms","call","text","voicemail",
        "sim card","carrier","provider","plan","contract",
        "5g","4g","lte","wifi","hotspot",
        "modem","router","broadband","fiber","cable",
        "telecom company", "telecommunication", "telephony", "telecom industry", "telecom services",
        "network", "wifi", "internet",
        "signal", "jio", "airtel", "5g", "4g", "lte", "roaming", "data", "sms", "mms", "call", "text", "voicemail",
        "sim card", "carrier", "provider", "plan", "contract",
        "vodafone", "reliance", "bsnl", "idea", "tata", "telecom operator", "telecom provider", "telecom network",
    ],
    "Transportation":[
        "car","bus","train","plane","bicycle",
        "motorcycle","ship","boat","subway","tram",
        "taxi","uber","lyft","public transport","traffic",
        "road","highway","bridge","tunnel","parking",
        "fuel","electric vehicle","autonomous vehicle","ride-sharing","commute",
        "transportation system", "transportation infrastructure", "transportation network", "transportation services", "transportation industry",
        "car", "bus", "train", "plane", "bicycle", "motorcycle", "ship", "boat", "subway", "tram",
        "taxi", "uber", "lyft", "public transport", "traffic",
        "road", "highway", "bridge", "tunnel", "parking",
    ],
    "Gaming":[
        "game","console","pc","xbox","playstation",
        "nintendo","steam","epic games","fortnite","minecraft",
        "call of duty","league of legends","dota 2","overwatch","apex legends",
        "gamer","gaming community","esports","tournament","streaming",
        "twitch","youtube gaming","game development","game design","game engine",
        "virtual reality", "augmented reality", "mixed reality", "game mechanics", "gameplay",
        "multiplayer", "single player", "co-op", "competitive", "casual",
        "valorant","counter-strike","pubg","world of warcraft","league of legends",
    ],
    "Health":[
        "health","fitness","exercise","nutrition","wellness", 
        "medicine","doctor","hospital","clinic","pharmacy",
        "disease","illness","symptom","treatment","cure",
        "mental health","therapy","counseling","support group","self-care",
        "healthcare system", "healthcare industry", "healthcare services", "healthcare"

    ],
    "Finance":[
        "finance","money","investment","stock","market",
        "bank","credit","debit","loan","mortgage",
        "interest rate","inflation","deflation","recession","economy",
        "cryptocurrency","bitcoin","ethereum","blockchain","decentralized finance",
        "financial planning", "financial management", "financial services", "financial industry", "financial market",

    ],
    "Education":[
        "education","school","university","college","teacher",
        "student","classroom","curriculum","homework","exam",
        "learning","teaching","knowledge","skill","training",
        "online education", "distance learning", "e-learning", "education technology", "education system",
        "CBSE", "ICSE", "state board", "higher education", "primary education",
        ],
    "Finance":[
        "finance","money","investment","stock","market",
        "bank","credit","debit","loan","mortgage",
        "interest rate","inflation","deflation","recession","economy",
        "cryptocurrency","bitcoin","ethereum","blockchain","decentralized finance",
        "financial planning", "financial management", "financial services", "financial industry", "financial market",

    ],
    "Social Media":[
        "social media","facebook","twitter","instagram","linkedin",
        "snapchat","tiktok","youtube","reddit","pinterest",
        "influencer","content creator","viral","hashtag","trending",
        "followers","likes","comments","shares","engagement",
        "social media platform", "social media marketing", "social media strategy", "social media management", "social media analytics",
    ],
    "Food":[
        "food","cuisine","restaurant","recipe","cooking",
        "baking","grilling","frying","steaming","boiling",
        "vegetarian","vegan","gluten-free","dairy-free","keto",
        "italian cuisine", "chinese cuisine", "indian cuisine", "mexican cuisine", "french cuisine",
        "breakfast", "lunch", "dinner", "snack", "dessert",
        "khana", "roti", "sabzi", "dal", "paneer","aloo","chicken","fish","egg","rice",
        "chaat","samosa","biryani","pasta","pizza",
    ]
}

# Theme Detection Function

def detect_themes(text):
    

    detected_themes = {}

    # Convert text to lowercase
    text = text.lower()

    # Loop through themes
    for theme, keywords in themes.items():

        matched_keywords = []

        # Check keywords
        for keyword in keywords:

            if keyword in text:

                matched_keywords.append(keyword)

        # Store theme if keywords found
        if matched_keywords:

            detected_themes[theme] = matched_keywords

    return detected_themes

# Aspect-Based Sentiment Analysis Function

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def analyze_aspects(text, detected_themes):

    aspect_sentiments = {}

    text = text.lower()

    # Split sentence into words
    words = text.split()

    # Flatten all keywords
    all_keywords = []

    for theme_keywords in detected_themes.values():

        all_keywords.extend(theme_keywords)

    # Analyze every keyword
    for keyword in all_keywords:

        if keyword in words:

            # Find keyword index
            idx = words.index(keyword)

            # Context window
            start = max(0, idx - 3)
            end = min(len(words), idx + 4)

            context = " ".join(words[start:end])

            # Analyze local context
            scores = analyzer.polarity_scores(context)

            compound = scores['compound']

            # Sentiment decision
            if compound >= 0.20:

                sentiment = "Positive"

            elif compound <= -0.20:

                sentiment = "Negative"

            else:

                sentiment = "Neutral"

            aspect_sentiments[keyword] = sentiment

    return aspect_sentiments