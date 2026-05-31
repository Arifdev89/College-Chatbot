import re

FAQ = {
    # FEES & COURSES
    "fees": "Our college offers the following fee structure:\n- B.E / B.Tech: ₹80,000/year\n- MBA: ₹60,000/year\n- MCA: ₹55,000/year\nScholarships are available for merit students.",
    "course": "We offer the following courses:\n- B.E in CSE, ECE, Mechanical, Civil\n- MBA\n- MCA\nAll programs are VTU affiliated.",
    "cse": "B.E in Computer Science (CSE) is a 4-year program affiliated to VTU. Fees: ₹80,000/year. Strong placement record with top IT companies.",
    "ece": "B.E in Electronics & Communication (ECE) is a 4-year VTU program. Fees: ₹80,000/year.",
    "mba": "MBA is a 2-year program. Fees: ₹60,000/year. Specializations: Finance, Marketing, HR.",
    "mca": "MCA is a 3-year program. Fees: ₹55,000/year. Focused on software development and IT.",
    "scholarship": "Scholarships are available for:\n- Government SC/ST scholarships\n- Merit-based fee waiver (top 5% students)\n- Sports quota scholarships\nContact the admin office for details.",

    # PLACEMENTS & SALARY
    "placement": "Our placement record is excellent!\n- 90%+ placement rate\n- Top recruiters: TCS, Infosys, Wipro, Accenture, IBM\n- Highest package: ₹18 LPA\n- Average package: ₹4.5 LPA",
    "salary": "Salary packages offered:\n- Highest: ₹18 LPA\n- Average: ₹4.5 LPA\n- Minimum: ₹3 LPA\nMost students get placed in top IT companies.",
    "recruiter": "Top recruiters visiting our campus:\nTCS, Infosys, Wipro, Accenture, IBM, Cognizant, Capgemini, HCL, Amazon, Deloitte.",
    "package": "Package details:\n- Highest CTC: ₹18 LPA\n- Average CTC: ₹4.5 LPA\n- More than 50 companies visit every year.",
    "internship": "Internship opportunities are provided in 6th semester. Companies like TCS, Infosys, and startups offer internships. Many students get PPO (Pre-Placement Offers).",

    # ADMISSION PROCESS
    "admission": "Admission Process:\n1. Fill online application at our website\n2. Submit 10th & 12th marksheets\n3. CET / COMEDK score required\n4. Document verification\n5. Fee payment\nContact: admissions@vvit.edu",
    "eligibility": "Eligibility Criteria:\n- B.E/B.Tech: 10+2 with PCM, min 45% marks\n- MBA: Any degree graduate with min 50%\n- MCA: BCA/BSc with Mathematics\nKarnataka CET or COMEDK score required.",
    "document": "Documents required for admission:\n- 10th Marksheet\n- 12th Marksheet\n- CET / COMEDK scorecard\n- Transfer Certificate\n- Aadhar Card\n- Passport size photos",
    "apply": "To apply:\n1. Visit our website\n2. Click on 'Apply Now'\n3. Fill the form and upload documents\n4. Pay application fee ₹500\nOr visit the campus directly at Bengaluru.",
    "last date": "Last date for admission is usually July 31st every year. For exact dates check our official website or call: 080-XXXXXXXX.",
    "cet": "Karnataka CET score is required for B.E admissions. COMEDK score is also accepted. Management quota seats are available without CET.",

    # HOSTEL & CAMPUS LIFE
    "hostel": "Hostel Facilities:\n- Separate boys and girls hostels\n- Fees: ₹60,000/year (food included)\n- 24/7 security and WiFi\n- Mess with hygienic food\n- AC and Non-AC rooms available",
    "campus": "Our campus features:\n- Modern classrooms and labs\n- Library with 10,000+ books\n- Sports ground (cricket, football, basketball)\n- Cafeteria and food court\n- WiFi enabled campus\n- Seminar halls and auditorium",
    "food": "Campus food options:\n- Hostel mess (included in hostel fee)\n- College cafeteria\n- Food court with multiple stalls\nVegetarian and non-vegetarian options available.",
    "wifi": "WiFi is available across the entire campus including classrooms, library, and hostel. Speed: 1 Gbps fiber connection.",
    "sports": "Sports facilities available:\n- Cricket ground\n- Football field\n- Basketball court\n- Indoor badminton\n- Table tennis\n- Gym\nAnnual sports fest is conducted every year.",
    "library": "Our library has:\n- 10,000+ books\n- Digital library access\n- Research journals and magazines\n- Study rooms\n- Open from 8 AM to 8 PM",
    "lab": "We have state-of-the-art labs:\n- Computer labs (500+ systems)\n- Electronics lab\n- Physics and Chemistry lab\n- Research and Innovation lab\n- All labs have latest equipment",

    # GENERAL
    "location": "Our college is located in Bengaluru, Karnataka, India. Well connected by BMTC buses and metro.",
    "contact": "Contact us:\n📞 Phone: 080-XXXXXXXX\n📧 Email: info@vvit.edu\n🌐 Website: www.vvit.edu\n📍 Address: Bengaluru, Karnataka",
    "affiliation": "Our college is affiliated to Visvesvaraya Technological University (VTU), Belagavi. AICTE approved and NAAC accredited.",
    "ranking": "Our college is ranked among the top engineering colleges in Karnataka. NAAC A grade accredited.",
    "naac": "Our college is NAAC accredited with A grade. This ensures quality education and better placement opportunities.",
}

GREETINGS = ['hi', 'hello', 'hey', 'good morning', 'good evening', 'good afternoon', 'hii', 'helo']

THANKS = ['thank', 'thanks', 'thank you', 'ok thanks', 'okay', 'great', 'awesome', 'nice']

def get_response(message):
    msg = message.lower().strip()

    # Greeting
    if any(g in msg for g in GREETINGS):
        return "👋 Hello! Welcome to VVIT Admissions Chatbot.\n\nI can help you with:\n- 💰 Fees & Courses\n- 🎯 Placements & Salary\n- 📝 Admission Process\n- 🏠 Hostel & Campus Life\n\nWhat would you like to know?"

    # Thanks
    if any(t in msg for t in THANKS):
        return "😊 You're welcome! Feel free to ask anything else about our college. We'd love to have you join VVIT!"

    # Match FAQ keywords
    for keyword, response in FAQ.items():
        if keyword in msg:
            return response

    # Fallback
    return "🤔 I'm not sure about that. You can ask me about:\n- Fees & Courses\n- Placements\n- Admission Process\n- Hostel & Campus\n\nOr contact us at 📞 080-XXXXXXXX or 📧 info@vvit.edu"
