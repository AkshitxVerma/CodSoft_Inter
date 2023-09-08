import random
from nltk.chat.util import Chat, reflections

pairs = [
    #General
    [
        r"hi|hey|hello",
        ["Hello!", "Hi there!", "Hey!", "Hi! How may I assist you?"]
    ],
    [
        r"how are you|how is everything",
        ["I'm doing well, thank you for asking!", "Everything is going great. How about you?", "I'm fine, thank you!", "I'm doing good. How are you?"]
    ],
    [
        r"what are you doing",
        ["I'm waiting to chat with you.", "I'm here to help you out.", "I'm ready to assist you with any questions."]
    ],
    [
        r"what are your hobbies| what is your favourite thing to do",
        ["I'm a chatbot, so chatting is my favourite thing to do!", "I enjoy interacting with people like you.", "Chatting with users like you is what I love to do."]
    ],
    [
        r"what can you do|what do you do",
        ["I can help you with a variety of tasks, like answering questions or providing suggestions.", "I'm here to assist you with any queries you have.", "I'm capable of answering a wide range of questions."]
    ],
    [
        r"what is your name|what can i call you|who are you",
        ["My name is QwertyBot, nice to meet you!", "You can call me QwertyBot.", "I'm QwertyBot, your virtual assistant."]
    ],
     [
        r"where are you from|where do you live|where are you located",
        ["I exist in the digital realm, so you can find me online!", "I'm a virtual assistant, so I don't have a physical location.", "I'm everywhere and nowhere at the same time, residing in the digital universe."]
    ],
    [
        r"how old are you| what is your age|when is your birthday",
        [ "I'm a Virtual Assistant, I don't have birthdays","I was created in a corner of the home library 2 days ago"]
    ],
    [
        r"tell me about yourself|introduce yourself",
        ["I am an AI-powered chatbot designed to assist and interact with users like you.", "I'm a virtual assistant capable of answering your questions and providing information.", "I'm an AI language model created by OpenAI to offer support and engage in conversations."]
    ],
    [
        r"what are your interests|what do you like to do in your free time",
        ["As a chatbot, I don't have personal interests or free time. I'm dedicated to assisting users like you.", "My main focus is to provide helpful information and engage in conversations."]
    ],
    #Greetings
    [
        r"bye|goodbye",
        ["Goodbye!", "See you later!", "Have a nice day!", "Farewell!", "Take care!"]
    ],
    [
        r"thanks|thank you",
        ["You're welcome!", "No problem.", "My pleasure.", "You're welcome! Happy to help.", "Glad I could assist you."]
    ],
    [
        r"good morning",
        ["Good Morning!", "With the new day comes new strength and new thoughts", "Have a wonderful start to your day"]
    ],
    [
        r'good evening',
        ["Good Evening!","How your day?","What did your day look like?"]
    ],
    #motivation
    [
        r"what is the best way to stay motivated|stay motivated|have motivation|best way i can have motivation",
        ["Staying motivated can be achieved by setting goals, breaking them down into smaller tasks, rewarding yourself, and finding inspiration from within or external sources.", "To stay motivated, it helps to maintain a positive mindset, surround yourself with supportive individuals, and regularly remind yourself of your goals."]
    ],
    [
        r"how can i stay motivated|tips for staying motivated|how to stay motivated",
        ["Staying motivated involves finding and maintaining the drive to pursue your goals. It can include practices like setting clear and meaningful goals, breaking them into smaller milestones, visualizing success, seeking inspiration from role models, and cultivating a positive mindset.", "To stay motivated, it helps to maintain a growth mindset, celebrate small wins, seek support from others, practice self-care, and regularly remind yourself of your why."]
    ],
    [
        r"how can i stay motivated when facing challenges|how to stay motivated in difficult times",
        ["To stay motivated when facing challenges, remind yourself of your goals and reasons for pursuing them. Break tasks into smaller steps, seek support from others, focus on progress rather than perfection, practice self-compassion, and celebrate small wins along the way.", "Maintain a positive mindset, visualize success, learn from setbacks, find inspiration from role models, and cultivate a supportive and encouraging environment."]
    ],
    [
        r"what are some effective ways to stay motivated when pursuing goals| how to stay motivated while completing a goal",
        ["To stay motivated when pursuing goals, set clear and specific goals, break them down into smaller milestones, visualize success, surround yourself with supportive and like-minded individuals, reward yourself for progress, and remind yourself of the reasons why you started.", "Practice self-reflection, maintain a positive mindset, track your progress, learn from setbacks, and seek inspiration from books, podcasts, or motivational speakers."]
    ],
    #growth
    [
        r"how can i improve my communication skills|how to improve communication skills",
        ["Improving communication skills can be done through active listening, practicing effective speaking, seeking feedback, and continuously learning and adapting to different situations.", "To enhance communication skills, it's beneficial to engage in meaningful conversations, read literature, and seek opportunities for public speaking or presentation."]
    ],
    [
        r"tell me about personal growth|How can i grow as an individual|what is personal growth|personal growth",
        ["Personal growth is an ongoing journey of self-improvement, self-awareness, and continuous learning. It involves setting goals, challenging yourself, embracing new experiences, and reflecting on your strengths and weaknesses.", "To grow as an individual, it's helpful to engage in self-reflection, seek feedback, step out of your comfort zone, and pursue lifelong learning."]
    ],
    [
        r"what are some effective goal-setting strategies|how to set my goals effectively",
        ["Effective goal-setting involves setting specific, measurable, achievable, relevant, and time-bound (SMART) goals. It's important to break them down into actionable steps, track progress, stay motivated, and adjust as needed.", "To set effective goals, consider your values, prioritize them, set milestones, create an action plan, and regularly review and update your goals."]
    ],
    [
        r"what are some self-reflection exercises i can try|how can i practice self reflection|self reflection excercises",
        ["Self-reflection exercises can include journaling, meditation, mindfulness practices, asking yourself meaningful questions, seeking feedback from others, and regularly reviewing your progress and experiences.", "To engage in self-reflection, take time for introspection, analyze your thoughts and emotions, identify patterns, and explore personal growth opportunities."]
    ],
    [
        r"how can i develop healthy habits for long-term success|develop healthy habits towards success|habits for success",
        ["To develop healthy habits for long-term success, start small and gradually introduce new habits, set realistic goals, practice consistency, build routines, track your progress, seek support from accountability partners, and celebrate milestones along the way.", "Focus on one habit at a time, create an environment that supports your goals, practice self-reflection, and be patient with yourself as habits take time to develop."]
    ],
    [
        r"how can i boost my self-confidence|how to be more confident",
        ["To boost self-confidence, focus on your strengths and accomplishments, practice self-compassion and positive self-talk, set achievable goals, step out of your comfort zone, surround yourself with supportive people, and celebrate your achievements.", "Dress in a way that makes you feel confident, practice good posture, learn new skills or hobbies, and seek professional help if low self-confidence persists."]
    ],
    [
        r"what are some effective techniques for overcoming challenges and setbacks|how to face up and downs",
        ["Effective techniques for overcoming challenges and setbacks include reframing failures as learning opportunities, practicing resilience and perseverance, seeking support from others, breaking challenges into smaller, manageable steps, and maintaining a positive mindset.", "Learn from past experiences, celebrate small victories, practice self-care during difficult times, and remind yourself of your strengths and past accomplishments."]
    ],
    [
        r"what are some effective techniques for setting and achieving goals|how to achieve goals",
        ["Effective techniques for setting and achieving goals include setting SMART goals (Specific, Measurable, Achievable, Relevant, Time-bound), breaking them down into actionable steps, tracking your progress, seeking accountability through a mentor or friend, and celebrating milestones along the way.", "Create a vision board, visualize success, develop a plan with deadlines, and regularly review and adjust your goals as needed."]
    ],
    [
        r"how can i cultivate a growth mindset|how to increase perspective of mind",
        ["To cultivate a growth mindset, embrace challenges as opportunities for growth, view failures as learning experiences, practice self-reflection and self-awareness, seek feedback as a chance for improvement, and believe in the power of effort and persistence.", "Surround yourself with positive and supportive individuals, read books or listen to podcasts that promote a growth mindset, and engage in activities that stretch your abilities and expand your horizons."]
    ],
    #study
    [
        r"what is the best way to learn a new language|how to learn new language",
        ["Learning a new language can be enhanced through consistent practice, immersing yourself in the language, using language learning apps or resources, and seeking opportunities to interact with native speakers.", "To learn a new language effectively, it's helpful to engage in regular conversation, practice reading and writing, and utilize language learning tools or courses."]
    ],
    [
        r"how can i study effectively|tips for effective studying|not able to study",
        ["Effective studying involves adopting strategies that help you learn and retain information more efficiently. It can include practices like creating a study schedule, organizing study materials, using active learning techniques, seeking clarification when needed, and reviewing and summarizing key concepts.", "To study effectively, it's beneficial to create a conducive study environment, manage your time effectively, utilize mnemonic devices, practice retrieval techniques, and engage in regular self-assessment."]
    ],
    [
        r"what are some study techniques for better retention|study techniques",
        ["Effective study techniques for better retention include active learning methods like summarizing information in your own words, teaching others, using mnemonic devices, practicing retrieval through quizzes or flashcards, and spacing out study sessions over time.", "To improve retention, engage in regular reviews, test yourself on the material, create visual aids, seek clarification when needed, and vary your study environment."]
    ],
    [
        r"what are some effective strategies for setting and achieving study goals|study goals",
        ["To set and achieve study goals, start by identifying specific learning objectives, break them down into manageable tasks, create a study schedule, utilize active learning techniques, seek support from classmates or teachers, and track your progress.", "Stay organized, practice self-discipline, review and revise your study strategies, seek clarification when needed, and regularly evaluate and adjust your study goals."]
    ],
    [
        r"what are some effective strategies for managing time during exam preparation|time management during exams",
        ["Effective strategies for managing time during exam preparation include creating a study schedule or timetable, prioritizing topics based on importance or difficulty, practicing active learning techniques, taking short breaks between study sessions, seeking clarification on challenging concepts, and reviewing and revising regularly.", "Eliminate distractions, break larger tasks into smaller study sessions, practice past exam papers, and seek support from teachers, classmates, or online resources."]
    ],
    #self-care
    [
        r"what is the best way to manage stress|how to deal with stress",
        ["Managing stress can involve practices like regular exercise, deep breathing exercises, practicing mindfulness or meditation, seeking social support, and engaging in activities you enjoy.", "To manage stress effectively, it's important to prioritize self-care, maintain a healthy lifestyle, and find healthy coping mechanisms that work for you."]
    ],
    [
        r"what are some self-care practices?|how can i take care of myself",
        ["Self-care involves engaging in activities that promote your physical, mental, and emotional well-being. It can include practices like exercise, meditation, getting enough sleep, pursuing hobbies, spending time in nature, practicing mindfulness, and seeking support when needed.", "To take care of yourself, it's important to prioritize rest, nourish your body with healthy food, engage in activities that bring you joy, and take breaks when you need them."]
    ],
    [
        r"how can i practice self-care on a busy schedule|self care for busy day",
        ["Practicing self-care on a busy schedule involves prioritizing and making time for activities that nourish your well-being. It can include quick self-care rituals like taking short breaks, practicing deep breathing, engaging in hobbies, and setting boundaries to protect your time.", "To practice self-care with a busy schedule, identify small pockets of time for self-care, integrate self-care into your routine, delegate tasks, and practice efficient time management."]
    ],
    [
        r"what are some effective self-care practices for mental well-being|mental health excercise|healthy mental being",
        ["Effective self-care practices for mental well-being include engaging in activities that promote relaxation and stress relief, such as practicing mindfulness or meditation, journaling, seeking therapy or counseling, connecting with loved ones, and engaging in hobbies or creative outlets.", "Prioritize self-compassion, establish healthy boundaries, practice self-reflection, take breaks when needed, and seek professional help if you're struggling with your mental health."]
    ],
    [
        r"what are some effective self-care practices for physical well-being|physical well being excercise|healthy physical being",
        ["Effective self-care practices for physical well-being include regular exercise, getting enough sleep, maintaining a balanced diet, staying hydrated, practicing good hygiene, and scheduling regular check-ups with healthcare professionals.", "Engage in activities that promote relaxation and stress relief, such as yoga, massage, or taking soothing baths. Take breaks from screens and practice good posture to support physical well-being."]
    ],
    #self love
    [
        r"how can i practice self love?|Tell me about self love|self love",
        ["Self-love is about nurturing a positive relationship with yourself, accepting who you are, and prioritizing your well-being. It involves practicing self-care, setting boundaries, embracing self-compassion, and celebrating your achievements and strengths.", "To practice self-love, it's important to prioritize self-care activities, engage in positive self-talk, surround yourself with supportive people, and practice forgiveness and self-acceptance."]
    ],
    [
        r"how can i build a positive body image|positive body image|body image issues",
        ["To build a positive body image, focus on what your body can do rather than just how it looks." ,"Practice self-care and treat your body with kindness and respect." ,"Surround yourself with positive influences and avoid comparing yourself to others."]
    ],
    [
        r"how can i maintain a healthy work-life balance|work life balance",
        ["To maintain a healthy work-life balance, set boundaries between work and personal life, prioritize self-care and leisure activities, delegate tasks when possible, practice effective time management, communicate your needs to supervisors or colleagues, and unplug from work during designated relaxation time.", "Schedule regular breaks, set realistic expectations, learn to say no to non-essential commitments, and create dedicated time for activities that bring you joy and fulfillment outside of work."]
    ],
    [
        r"what are some effective techniques for managing and reducing anxiety|anxiety excercises|manage anxiety",
        ["Effective techniques for managing and reducing anxiety include deep breathing exercises, practicing mindfulness or meditation, engaging in regular physical exercise, challenging negative thoughts, seeking professional help or therapy, and maintaining a healthy lifestyle with proper nutrition and sleep.", "Identify triggers and develop coping strategies, create a support network, and engage in activities that promote relaxation, such as listening to calming music or spending time in nature."]
    ],
    #productivity
    [
        r"how can i improve my productivity|tips for being more productive|how can i be more productive",
        ["Improving productivity involves optimizing your time, focus, and energy to accomplish tasks efficiently. It can include practices like setting clear goals, prioritizing tasks, breaking them into smaller steps, managing distractions, and practicing effective time management techniques.", "To enhance productivity, it's helpful to establish routines, eliminate or delegate non-essential tasks, take regular breaks, utilize productivity tools, and maintain a healthy work-life balance."]
    ],
    [
        r"what are some effective time management techniques| time management techniques|time management",
        ["Effective time management techniques include prioritizing tasks, creating schedules or to-do lists, using productivity tools, implementing the Pomodoro Technique (working in focused bursts with breaks), and avoiding multitasking.", "To manage your time effectively, set realistic deadlines, eliminate time-wasting activities, delegate tasks when possible, and maintain a balance between work and relaxation."]
    ],
    [
        r"what are some effective stress management techniques|ways to manage stress|stress management",
        ["Effective stress management techniques include practicing relaxation techniques like deep breathing or meditation, engaging in physical activity, getting enough sleep, maintaining a healthy diet, seeking social support, and engaging in activities that bring you joy.", "To manage stress effectively, establish boundaries, prioritize self-care, delegate tasks when possible, practice time management, and engage in stress-reducing activities like hobbies or spending time in nature."]
    ],
    [
        r"what are some effective ways to improve focus and concentration|imrove focus|focus and concentration excercises",
        ["To improve focus and concentration, eliminate distractions like turning off notifications, create a conducive environment for concentration, practice mindfulness or meditation, break tasks into manageable chunks, set specific goals, and take regular breaks to refresh your mind.", "Establish a routine, prioritize tasks, maintain a healthy lifestyle, organize your workspace, and use techniques like the Pomodoro Technique or time-blocking to enhance focus."]
    ],
    [
        r"how can i develop a positive mindset|develop mindset",
        ["Developing a positive mindset involves practicing gratitude, reframing negative thoughts into positive ones, surrounding yourself with positive influences, focusing on solutions rather than problems, and engaging in self-affirmations or positive self-talk.", "Challenge self-limiting beliefs, practice self-compassion, embrace failures as learning opportunities, visualize success, and seek inspiration from motivational resources or role models."]
    ],
    [
        r"how can i cultivate a healthy work-life balance|healthy work life balance",
        ["To cultivate a healthy work-life balance, set clear boundaries between work and personal life, prioritize self-care and leisure activities, practice time management, communicate your needs with your employer or colleagues, delegate tasks when possible, and disconnect from work during your non-working hours.", "Learn to say no, establish a routine that allows for work and personal time, create designated spaces for work and relaxation, and regularly evaluate and adjust your priorities."]
    ],
    [
        r"How can I overcome procrastination and improve productivity|be more productive|how can i be more productive",
        ["To overcome procrastination and improve productivity, break tasks into smaller, more manageable steps, set deadlines for each step, eliminate distractions, use productivity tools or apps, create a reward system, and practice self-accountability.", "Visualize the benefits of completing the task, identify and address underlying reasons for procrastination, seek support from an accountability partner, and create a motivating work environment."]
    ],
    [
        r"what are some effective strategies for managing work-related stress|work stress management",
        ["To manage work-related stress, prioritize tasks, communicate with your supervisor or team about your workload, practice time management techniques, delegate tasks when possible, seek support from colleagues, and engage in stress-reducing activities outside of work.", "Set boundaries between work and personal life, practice relaxation techniques, maintain a healthy work-life balance, and prioritize self-care activities to reduce stress."]
    ],
    [
        r"what are some effective ways to enhance creativity and innovation|be more creative|be more innovative|how to be more creative|how to be more innovative",
        ["To enhance creativity and innovation, engage in activities that inspire you, such as reading, exploring different art forms, trying new experiences, practicing mindfulness or meditation, collaborating with others, and allowing yourself to take risks and embrace failure.", "Step out of your comfort zone, expose yourself to diverse perspectives and ideas, and create a conducive environment that encourages creativity, such as organizing a dedicated workspace or setting aside regular time for brainstorming."]
    ],
    [
        r"what are some effective strategies for increasing productivity|how to increase productivity",
        ["Effective strategies for increasing productivity include setting clear goals and priorities, eliminating distractions, using time management techniques, breaking tasks into smaller steps, using productivity tools or apps, delegating tasks when possible, and practicing self-discipline.", "Create a productive work environment, set realistic deadlines, take regular breaks, and establish a routine that supports productivity."]
    ],  
    #finance
    [
        r"what is the best way to save money|how can i save money|how can i start saving",
        ["Saving money can be achieved by creating a budget, tracking expenses, cutting unnecessary costs, and setting financial goals. It's also helpful to automate savings and seek professional advice if needed.", "To save money effectively, it's beneficial to practice frugality, avoid impulsive purchases, and allocate a portion of your income towards savings."]
    ],
    [
        r"how can i manage my finances better?|tips for financial management|financial management",
        ["Managing finances effectively involves budgeting, saving, investing wisely, and making informed financial decisions. It can include practices like tracking expenses, creating a budget, setting financial goals, minimizing debt, diversifying income streams, and seeking professional advice when needed.", "To manage finances better, it's important to cultivate financial literacy, practice frugality, differentiate between needs and wants, plan for the future, and regularly review and adjust your financial strategy."]
    ],
    [
        r"what are some effective strategies for saving money|mmoney saving tips|savings tip",
        ["Effective strategies for saving money include creating a budget, tracking expenses, identifying areas where you can cut back, automating savings, setting financial goals, avoiding impulse purchases, and exploring ways to increase your income.", "To save money effectively, differentiate between needs and wants, negotiate better deals, plan meals and shop with a grocery list, review and optimize your recurring expenses, and avoid unnecessary fees."]
    ],
    [
        r"hat are some ways to reduce debt and improve financial health|reduce debt",
        ["To reduce debt and improve financial health, prioritize paying off high-interest debt first, create a debt repayment plan, explore options like debt consolidation or balance transfers, negotiate with creditors, and seek professional advice if needed.", "To improve financial health, track and analyze your spending, cut unnecessary expenses, build an emergency fund, invest in your future, and educate yourself about personal finance."]
    ],
    [
        r"how can i improve my financial literacy|financial literacy|gain financial literacy",
        ["To improve financial literacy, read books or articles on personal finance, follow reputable financial websites or blogs, take online courses or workshops, listen to podcasts on finance, join financial communities or forums, and consult with financial advisors.", "Stay updated on financial news and trends, practice budgeting and tracking expenses, understand investment options, and seek guidance to make informed financial decisions."]
    ],
    [
        r"what are some effective strategies for setting and achieving financial goals|reach financial goals|set financial goals",
        ["To set and achieve financial goals, start by identifying your short-term, medium-term, and long-term goals. Break them down into actionable steps, create a timeline, track your progress, adjust as needed, and celebrate milestones along the way.", "Automate savings, diversify your income, invest wisely, minimize debt, educate yourself about personal finance, and seek guidance from financial professionals to make informed financial decisions."]
    ],
    [
        r"what are some effective strategies for managing personal finances as a student|student finance",
        ["To manage personal finances as a student, create a budget, track your expenses, prioritize needs over wants, look for student discounts or scholarships, explore part-time job opportunities, save money on textbooks or study materials, and plan for student loan repayment.", "Seek financial aid or grants, educate yourself about student loan options, consider alternative transportation methods, and explore opportunities for financial assistance or scholarships."]
    ],
    [
        r"what are some effective strategies for building a savings habit|habit of saving",
        ["To build a savings habit, automate your savings by setting up automatic transfers to a savings account, create a budget that includes savings goals, track your expenses, avoid unnecessary purchases, and look for opportunities to save money through discounts or coupons.", "Find ways to increase your income, such as taking on a side gig or freelancing, and regularly review your savings plan to ensure it aligns with your financial goals."]
    ],
    [
        r"how can i manage my finances effectively during a financial crisis|finance during crisis",
        ["To manage finances effectively during a financial crisis, prioritize essential expenses, create a revised budget, explore financial assistance options or relief programs, communicate with creditors or lenders to negotiate payment terms, and seek professional financial advice if needed.", "Look for ways to increase income, minimize non-essential expenses, and utilize resources and support from community organizations or government programs."]
    ],
    [
        r"what are some effective strategies for effective financial planning|financial planning",
        ["Effective strategies for effective financial planning include setting financial goals, creating a budget, tracking expenses, reducing debt, saving for emergencies, investing for the future, regularly reviewing and adjusting your financial plan, and seeking professional financial advice when needed.", "Educate yourself on personal finance topics, build an emergency fund, diversify your investments, and prioritize long-term financial security."]
    ],
    [
        r"how can i develop a positive money mindset|develop a money mindset",
        ["To develop a positive money mindset, practice gratitude for what you have, focus on abundance rather than scarcity, challenge limiting beliefs about money, educate yourself about personal finance, set financial goals aligned with your values, and celebrate your financial achievements.", "Surround yourself with positive financial influences, create a healthy relationship with money, and practice mindful spending and saving."]
    ],
    #no queries match
    [
         r"(.*)",
         ["Sorry, I couldn't get that. How may I assist you?"]
    ]
]

chatbot = Chat(pairs, reflections)

def respond(message):
    return chatbot.respond(message)

while True:
    message = input("You: ")
    response = respond(message)

    print("QwertyBot:", response)
        

