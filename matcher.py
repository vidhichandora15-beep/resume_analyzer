
# Text matching ke liye libraries import karna
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Resume aur job description ka similarity score
def calculate_match(resume_text, job_description):

    # Dono texts ko list mein store karna
    documents = [resume_text, job_description]

    # Text ko numerical values mein convert karna
    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(documents)

    # Dono texts ki similarity calculate karna
    score = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    # Score ko percentage mein convert karna
    return round(score * 100, 2)

# Resume ki skills ko job requirements se compare karna
def compare_skills(resume_text, job_description):

    # Skills ki list
    skills = [
        "python",
        "java",
        "html",
        "css",
        "javascript",
        "sql",
        "mysql",
        "machine learning",
        "data analysis",
        "pandas",
        "scikit-learn",
        "git",
        "communication",
        "problem solving"
    ]

    # Dono texts ko lowercase mein convert karna
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    # Job description mein required skills find karna
    required_skills = [
        skill for skill in skills
        if skill in job_description
    ]

    # Resume mein available matching skills find karna
    matched_skills = [
        skill for skill in required_skills
        if skill in resume_text
    ]

    # Resume mein missing skills find karna
    missing_skills = [
        skill for skill in required_skills
        if skill not in resume_text
    ]

    # Skill match percentage calculate karna
    if len(required_skills) > 0:

        skill_score = (
            len(matched_skills)
            / len(required_skills)
        ) * 100

    else:
        skill_score = 0

    # Saare results return karna
    return (
        matched_skills,
        missing_skills,
        round(skill_score, 2)
    )
