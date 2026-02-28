import streamlit as st

import question_1 as q1
import question_2 as q2
import question_3 as q3
import question_4 as q4

# Page configuration
st.set_page_config(
    page_title="AI Assignment 1",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f5f6fa;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        min-height: 100vh;
    }
    
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    
    .subtitle {
        text-align: center;
        color: #7f8c8d;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 3rem;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        border: 2px solid #e67e22;
        background-color: #f39c12;
        color: white;
    }
    
    .stButton > button:hover {
        background-color: #e67e22;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(230, 126, 34, 0.3);
    }
    
    .question-card {
        background: #ffffff;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border-left: 4px solid #e67e22;
    }
    
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #27ae60;
        margin: 0.5rem 0;
    }
    
    .results-table {
        background: white;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        border: 1px solid #ecf0f1;
    }
    
    .info-box {
        background: #34495e;
        color: white;
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        margin: 2rem 0;
    }
    
    .stSelectbox > div > div {
        border-radius: 8px;
    }
    
    .stNumberInput > div > div > input {
        border-radius: 8px;
    }
    
    h4 {
        color: #2c3e50;
        border-bottom: 2px solid #e67e22;
        padding-bottom: 0.5rem;
    }
    
    .stForm {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">AI Assignment 1</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Explore Knowledge Graphs, Case-Based Reasoning, Content Recommendation Chatbot & Maze Solving</p>', unsafe_allow_html=True)

# Keep the selected view across reruns
if "selected_question" not in st.session_state:
    st.session_state.selected_question = None

# Main navigation
st.markdown("### Choose your AI technique:")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Knowledge Graph", use_container_width=True):
        st.session_state.selected_question = "q1"

with col2:
    if st.button("Case-Based Reasoning", use_container_width=True):
        st.session_state.selected_question = "q2"

with col3:
    if st.button("Content Recommender Chatbot", use_container_width=True):
        st.session_state.selected_question = "q3"

with col4:
    if st.button("Maze Pathfinder", use_container_width=True):
        st.session_state.selected_question = "q4"

st.divider()

# ---- Question 1 UI (Knowledge Graph) ----
if st.session_state.selected_question == "q1":
    st.markdown('<div class="question-card">', unsafe_allow_html=True)
    
    st.markdown("## Knowledge Graph Explorer")
    st.markdown("*Discover relationships and properties in our semantic network*")
    
    col_select, col_empty = st.columns([2, 1])
    with col_select:
        entity = st.selectbox(
            "Select an entity/concept",
            options=q1.list_entities(),
            index=0,
        )

    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("#### Properties & Relations")
        if st.button("Show Properties", use_container_width=True):
            likes, is_in, painted = q1.get_properties(entity)
            
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.markdown("**Likes**")
            st.write(sorted(likes) if likes else "—")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.markdown("**Is In**")
            st.write(sorted(is_in) if is_in else "—")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.markdown("**Painted**")
            st.write(sorted(painted) if painted else "—")
            st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown("#### Inheritance Chain")
        if st.button("Show Is-A Chain", use_container_width=True):
            parents = q1.get_is_a(entity)
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.markdown("**Is A**")
            st.write(sorted(parents) if parents else "—")
            st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Question 2 UI (Case-Based Reasoning) ----
elif st.session_state.selected_question == "q2":
    st.markdown('<div class="question-card">', unsafe_allow_html=True)
    
    st.markdown("## Case-Based Reasoning")
    st.markdown("*Find similar cars based on your criteria*")

    with st.form("cbr_form"):
        st.markdown("#### Configure Your Car")
        
        c1, c2 = st.columns(2)

        with c1:
            st.markdown("**Engine & Performance**")
            cv = st.number_input("Engine Power (CV)", min_value=500, max_value=5000, value=1700, step=50)
            brand = st.selectbox("Brand", options=q2.list_brands(), index=0)
            mileage = st.number_input("Mileage", min_value=0, max_value=500000, value=45000, step=1000)

        with c2:
            st.markdown("**Efficiency & Aesthetics**")
            mpg = st.number_input("Mile/Gallon Rate", min_value=1, max_value=100, value=27, step=1)
            color = st.selectbox("Color", options=q2.list_colors(), index=0)
            price = st.number_input("Price ($)", min_value=0, max_value=200000, value=16500, step=500)

        k = st.slider("Number of Similar Cars to Find", min_value=1, max_value=min(10, len(q2.case_base)), value=3)

        submitted = st.form_submit_button("Find Similar Cars", use_container_width=True)

    if submitted:
        new_case = {
            "cv": int(cv),
            "brand": brand,
            "mileage": int(mileage),
            "mile gallon rate": int(mpg),
            "color": color,
            "price": int(price),
        }

        with st.spinner("Analyzing similar cars..."):
            results: list[dict[str, int | dict[str, int|str]]] = q2.find_best_matches(new_case, k=k)

        st.markdown("### Results")
        
        # Query summary
        col_q1, col_q2, col_q3 = st.columns(3)
        with col_q1:
            st.metric("Engine Power", f"{cv} CV")
            st.metric("Brand", brand)
        with col_q2:
            st.metric("Mileage", f"{mileage:,} miles")
            st.metric("Color", color)
        with col_q3:
            st.metric("Efficiency", f"{mpg} MPG")
            st.metric("Price", f"${price:,}")

        # Results table
        rows = []
        for rank, car_match in enumerate(results, 1):
            car_details = car_match["case"]
            rows.append({
                "Rank": rank,
                "Distance": round(int(car_match["distance"]), 2),
                "Brand": car_details["brand"],
                "Model": car_details.get("model", ""),
                "CV": car_details["cv"],
                "Mileage": f"{car_details['mileage']:,}",
                "MPG": car_details["mile gallon rate"],
                "Color": car_details["color"],
                "Price": f"${car_details['price']:,}",
            })

        st.markdown('<div class="results-table">', unsafe_allow_html=True)
        st.dataframe(rows, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Question 3 UI (Content Recommendation Chatbot) ----
elif st.session_state.selected_question == "q3":
    st.markdown('<div class="question-card">', unsafe_allow_html=True)
    
    st.markdown("## Content Recommendation Chatbot")
    st.markdown("*Chat with our bot to get personalized movie, series & digital content recommendations*")
    
    # Initialize chat history and state
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []
    if "chat_step" not in st.session_state:
        st.session_state.chat_step = 0
    if "chat_preferences" not in st.session_state:
        st.session_state.chat_preferences = {}
    if "chat_done" not in st.session_state:
        st.session_state.chat_done = False

    # Define the conversation flow
    CHAT_QUESTIONS = [
        {
            "key": "name",
            "question": " Hi there! I'm ContentBot, your personal entertainment assistant. What's your name?",
            "type": "free_text",
        },
        {
            "key": "content_type",
            "question": "Nice to meet you, {name}! What type of content are you in the mood for?",
            "type": "select",
            "options": ['Movie', 'TV Series', 'Documentary', 'Anime', 'Short Film',
                        'Stand-up Comedy', 'Kids Content', 'Reality Show', 'Talk Show',
                        'Cooking Show', 'Travel Show', 'Nature Documentary', 'True Crime'],
        },
        {
            "key": "genre",
            "question": "Great choice! What genre appeals to you today?",
            "type": "select",
            "options": ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
                        'Drama', 'Family', 'Fantasy', 'Horror', 'Musical', 'Mystery',
                        'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western', 'Sports',
                        'Historical', 'Psychological', 'Supernatural'],
        },
        {
            "key": "mood",
            "question": "What's your current mood? This helps me pick something that fits perfectly.",
            "type": "select",
            "options": ['Happy and Upbeat', 'Sad and Contemplative', 'Adventurous',
                        'Romantic', 'Thrilled/Excited', 'Relaxed', 'Curious/Learning',
                        'Nostalgic', 'Energetic', 'Thoughtful', 'Escapist'],
        },
        {
            "key": "time_available",
            "question": "How much time do you have for watching?",
            "type": "select",
            "options": ['Under 30 minutes', '30-60 minutes', '1-2 hours',
                        '2-3 hours', '3+ hours', 'Binge-watching session'],
        },
        {
            "key": "age_rating",
            "question": "What age rating are you comfortable with?",
            "type": "select",
            "options": ['G (General)', 'PG (Parental Guidance)', 'PG-13 (Teen)',
                        'R (Mature)', 'TV-Y (Kids)', 'TV-14 (Teen TV)',
                        'TV-MA (Mature TV)', 'No Preference'],
        },
        {
            "key": "language",
            "question": "Do you have a language preference?",
            "type": "select",
            "options": ['English', 'Spanish', 'French', 'German', 'Italian', 'Japanese',
                        'Korean', 'Chinese', 'Hindi', 'Arabic', 'Portuguese', 'Russian',
                        'Subtitled Foreign Films', 'No Preference'],
        },
        {
            "key": "platforms",
            "question": "Which streaming platforms do you have access to? (You can select multiple)",
            "type": "multiselect",
            "options": ['Netflix', 'Amazon Prime Video', 'Disney+', 'HBO Max', 'Hulu',
                        'Apple TV+', 'Paramount+', 'Peacock', 'YouTube Premium',
                        'Crunchyroll', 'Funimation', 'Free Platforms', 'Any Platform'],
        },
        {
            "key": "content_age",
            "question": "Do you prefer newer or older content?",
            "type": "select",
            "options": ['Brand New (2024-2026)', 'Recent (2020-2023)', 'Modern (2010-2019)',
                        'Classic (2000-2009)', 'Vintage (1990s)', 'Retro (1980s or older)', 'No Preference'],
        },
        {
            "key": "popularity",
            "question": "Do you prefer popular hits or hidden gems?",
            "type": "select",
            "options": ['Mainstream Blockbusters', 'Popular but Not Too Mainstream',
                        'Critically Acclaimed', 'Hidden Gems', 'Cult Classics', 'No Preference'],
        },
        {
            "key": "intensity",
            "question": "What emotional intensity are you looking for?",
            "type": "select",
            "options": ['Light and Fun', 'Moderate Emotions', 'Emotionally Intense',
                        'Heart-Wrenching', 'Mind-Bending', 'Adrenaline-Pumping', 'Peaceful and Calming'],
        },
        {
            "key": "company",
            "question": "Who will you be watching with?",
            "type": "select",
            "options": ['Alone', 'Romantic Partner', 'Family with Kids', 'Friends',
                        'Family (Adults Only)', 'Large Group'],
        },
        {
            "key": "setting",
            "question": "What kind of setting or world interests you?",
            "type": "select",
            "options": ['Modern Urban', 'Historical Period', 'Futuristic', 'Fantasy World',
                        'Small Town', 'Wilderness/Nature', 'Space', 'Underwater',
                        'Different Country/Culture', 'Post-Apocalyptic', 'Magical Realm', 'No Preference'],
        },
        {
            "key": "favorites",
            "question": "Do you have any favorite actors or directors? (Type names or say 'skip')",
            "type": "free_text",
        },
        {
            "key": "avoid",
            "question": "Anything you want to avoid in your content? (You can select multiple)",
            "type": "multiselect",
            "options": ['Violence', 'Horror/Scary', 'Sad Endings', 'Explicit Content',
                        'Slow Paced', 'Subtitles', 'Black and White', 'Musicals',
                        'Very Long Content', 'Cliffhangers', 'Nothing to Avoid'],
        },
        {
            "key": "specific_interest",
            "question": "Last question! Any specific themes or topics you're interested in? (Type anything or say 'skip')",
            "type": "free_text",
        },
    ]

    # Display chat history
    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Show first bot message
    if st.session_state.chat_step == 0 and not st.session_state.chat_messages:
        bot_msg = CHAT_QUESTIONS[0]["question"]
        st.session_state.chat_messages.append({"role": "assistant", "content": bot_msg})
        st.rerun()

    # If not done, show the appropriate input for current step
    if not st.session_state.chat_done and st.session_state.chat_step < len(CHAT_QUESTIONS):
        current_q = CHAT_QUESTIONS[st.session_state.chat_step]

        if current_q["type"] == "free_text":
            user_input = st.chat_input("Type your answer here...")
            if user_input:
                st.session_state.chat_messages.append({"role": "user", "content": user_input})
                st.session_state.chat_preferences[current_q["key"]] = user_input.strip()
                st.session_state.chat_step += 1

                if st.session_state.chat_step < len(CHAT_QUESTIONS):
                    next_q = CHAT_QUESTIONS[st.session_state.chat_step]
                    next_msg = next_q["question"].format(**st.session_state.chat_preferences)
                    st.session_state.chat_messages.append({"role": "assistant", "content": next_msg})
                else:
                    st.session_state.chat_done = True
                    st.session_state.chat_messages.append({"role": "assistant", "content": " Thanks! Let me find the best content for you..."})
                st.rerun()

        elif current_q["type"] == "select":
            with st.container():
                cols = st.columns(3)
                for idx, option in enumerate(current_q["options"]):
                    col = cols[idx % 3]
                    with col:
                        if st.button(option, key=f"chat_opt_{st.session_state.chat_step}_{idx}", use_container_width=True):
                            st.session_state.chat_messages.append({"role": "user", "content": option})
                            st.session_state.chat_preferences[current_q["key"]] = option.lower()
                            st.session_state.chat_step += 1

                            if st.session_state.chat_step < len(CHAT_QUESTIONS):
                                next_q = CHAT_QUESTIONS[st.session_state.chat_step]
                                next_msg = next_q["question"].format(**st.session_state.chat_preferences)
                                st.session_state.chat_messages.append({"role": "assistant", "content": next_msg})
                            else:
                                st.session_state.chat_done = True
                                st.session_state.chat_messages.append({"role": "assistant", "content": " Thanks! Let me find the best content for you..."})
                            st.rerun()

        elif current_q["type"] == "multiselect":
            selected = st.multiselect(
                "Select one or more options:",
                current_q["options"],
                key=f"chat_multi_{st.session_state.chat_step}"
            )
            if st.button("Confirm Selection", key=f"chat_confirm_{st.session_state.chat_step}"):
                if selected:
                    display_text = ", ".join(selected)
                    st.session_state.chat_messages.append({"role": "user", "content": display_text})
                    st.session_state.chat_preferences[current_q["key"]] = [s.lower() for s in selected]
                    st.session_state.chat_step += 1

                    if st.session_state.chat_step < len(CHAT_QUESTIONS):
                        next_q = CHAT_QUESTIONS[st.session_state.chat_step]
                        next_msg = next_q["question"].format(**st.session_state.chat_preferences)
                        st.session_state.chat_messages.append({"role": "assistant", "content": next_msg})
                    else:
                        st.session_state.chat_done = True
                        st.session_state.chat_messages.append({"role": "assistant", "content": " Thanks! Let me find the best content for you..."})
                    st.rerun()
                else:
                    st.warning("Please select at least one option!")

    # Generate and display recommendations when chat is done
    if st.session_state.chat_done:
        prefs = st.session_state.chat_preferences
        content_db = q3.create_content_database()

        # Build a compatible preferences dict for generate_recommendations
        rec_prefs = {
            "content_type": prefs.get("content_type", "movie"),
            "genre": prefs.get("genre", "action"),
            "mood": prefs.get("mood", "happy"),
            "platforms": prefs.get("platforms", ["any platform"]),
            "content_age": prefs.get("content_age", "no preference"),
            "setting": prefs.get("setting", "no preference"),
        }

        recommendations = q3.generate_recommendations(rec_prefs, content_db)

        if recommendations:
            rec_text = "## Here are my top recommendations for you!\n\n"
            for i, rec in enumerate(recommendations[:5], 1):
                c = rec["content"]
                rec_text += f"### #{i} — {c['title']}\n"
                rec_text += f"- **Type:** {c['type'].title()}\n"
                rec_text += f"- **Genre:** {c['genre'].title()}\n"
                rec_text += f"- **Year:** {c['year']}\n"
                rec_text += f"- **Rating:** {c['rating']}\n"
                rec_text += f"- **Platform:** {c['platform'].title()}\n"
                rec_text += f"- **Match Score:** {rec['score']}/25\n"
                if rec["reasons"]:
                    rec_text += f"- **Why:** {', '.join(rec['reasons'])}\n"
                rec_text += "\n"
            
            # Check if we already added the recommendations message
            if not any("Here are my top recommendations" in m["content"] for m in st.session_state.chat_messages):
                st.session_state.chat_messages.append({"role": "assistant", "content": rec_text})
                st.rerun()
        else:
            no_match_msg = " I couldn't find a perfect match with your criteria. Try adjusting some preferences!"
            if not any("couldn't find" in m["content"] for m in st.session_state.chat_messages):
                st.session_state.chat_messages.append({"role": "assistant", "content": no_match_msg})
                st.rerun()

        # Reset button
        if st.button(" Start New Conversation", use_container_width=True):
            st.session_state.chat_messages = []
            st.session_state.chat_step = 0
            st.session_state.chat_preferences = {}
            st.session_state.chat_done = False
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ---- Question 4 UI (Maze Pathfinder) ----
elif st.session_state.selected_question == "q4":
    st.markdown('<div class="question-card">', unsafe_allow_html=True)
    
    st.markdown("##  BFS Maze Pathfinder")
    st.markdown("*Set start and goal positions, then watch BFS find the shortest path!*")
    
    maze = q4.maze
    rows = len(maze)
    cols = len(maze[0])
    
    # Get valid (open) cells for start/goal selection
    open_cells = []
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 0:
                open_cells.append((r, c))
    
    open_cell_labels = [f"({r}, {c})" for r, c in open_cells]
    
    st.markdown("#### Configure Start & Goal")
    c1, c2 = st.columns(2)
    
    with c1:
        start_idx = st.selectbox(
            "🟢 Start Position (row, col)",
            options=range(len(open_cells)),
            format_func=lambda i: open_cell_labels[i],
            index=0,
        )
        start = open_cells[start_idx]
    
    with c2:
        # Default goal to last open cell
        default_goal_idx = len(open_cells) - 1
        goal_idx = st.selectbox(
            "🔴 Goal Position (row, col)",
            options=range(len(open_cells)),
            format_func=lambda i: open_cell_labels[i],
            index=default_goal_idx,
        )
        goal = open_cells[goal_idx]
    
    if start == goal:
        st.warning("Start and goal are the same cell. Please pick different positions.")
    
    if st.button("🔍 Find Path", use_container_width=True):
        path = q4.bfs_pathfinder(maze, start, goal)
        path_set = set(path) if path else set()
        
        if path:
            st.success(f" Path found! Length: **{len(path)} steps**")
        else:
            st.error(" No path found between these positions.")
        
        # Build the maze as an HTML table for nice visual rendering
        st.markdown("#### Maze Visualization")
        
        # Color legend
        st.markdown("""
        <div style="display:flex; gap:18px; margin-bottom:10px; flex-wrap:wrap;">
            <span>🟢 <b>Start</b></span>
            <span>🔴 <b>Goal</b></span>
            <span>🟡 <b>Path</b></span>
            <span>⬛ <b>Wall</b></span>
            <span>⬜ <b>Open</b></span>
        </div>
        """, unsafe_allow_html=True)
        
        cell_size = 18
        html = '<div style="overflow-x:auto;"><table style="border-collapse:collapse;margin:auto;">'
        for r in range(rows):
            html += "<tr>"
            for c in range(cols):
                if (r, c) == start:
                    color = "#27ae60"   # green
                    char = "S"
                    text_color = "white"
                elif (r, c) == goal:
                    color = "#e74c3c"   # red
                    char = "G"
                    text_color = "white"
                elif (r, c) in path_set:
                    color = "#f1c40f"   # yellow
                    char = "•"
                    text_color = "#333"
                elif maze[r][c] == 1:
                    color = "#2c3e50"   # dark wall
                    char = ""
                    text_color = "#2c3e50"
                else:
                    color = "#ecf0f1"   # light open
                    char = ""
                    text_color = "#ecf0f1"
                
                html += (
                    f'<td style="width:{cell_size}px;height:{cell_size}px;'
                    f'background:{color};text-align:center;font-size:10px;'
                    f'font-weight:bold;color:{text_color};padding:0;'
                    f'border:1px solid #bdc3c7;">{char}</td>'
                )
            html += "</tr>"
        html += "</table></div>"
        
        st.markdown(html, unsafe_allow_html=True)
        
        # Show path details
        if path:
            with st.expander(" View Full Path Coordinates"):
                path_str = " → ".join([f"({r},{c})" for r, c in path])
                st.code(path_str, language=None)
    else:
        # Show the plain maze without path
        st.markdown("#### Maze Preview")
        
        cell_size = 18
        html = '<div style="overflow-x:auto;"><table style="border-collapse:collapse;margin:auto;">'
        for r in range(rows):
            html += "<tr>"
            for c in range(cols):
                if (r, c) == start:
                    color = "#27ae60"
                    char = "S"
                    text_color = "white"
                elif (r, c) == goal:
                    color = "#e74c3c"
                    char = "G"
                    text_color = "white"
                elif maze[r][c] == 1:
                    color = "#2c3e50"
                    char = ""
                    text_color = "#2c3e50"
                else:
                    color = "#ecf0f1"
                    char = ""
                    text_color = "#ecf0f1"
                
                html += (
                    f'<td style="width:{cell_size}px;height:{cell_size}px;'
                    f'background:{color};text-align:center;font-size:10px;'
                    f'font-weight:bold;color:{text_color};padding:0;'
                    f'border:1px solid #bdc3c7;">{char}</td>'
                )
            html += "</tr>"
        html += "</table></div>"
        
        st.markdown(html, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="info-box">
        <h3>Welcome to AI Assignment 1</h3>
        <p>Select an option above to explore:</p>
        <p><strong>Knowledge Graph:</strong> Navigate semantic networks and discover relationships</p>
        <p><strong>Case-Based Reasoning:</strong> Find similar cases using distance metrics</p>
        <p><strong>Content Recommender Chatbot:</strong> Chat with a bot to get personalized movie & series recommendations</p>
        <p><strong>Maze Pathfinder:</strong> Visualize BFS pathfinding on a maze grid</p>
    </div>
    """, unsafe_allow_html=True)


