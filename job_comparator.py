# Matcher file se required functions import karna
from matcher import calculate_match, compare_skills

# Resume ko multiple jobs ke saath compare karna
def compare_jobs(resume_text, job_descriptions):

    # Results store karne ke liye empty list
    results = []

    # Har job description ko check karna
    for job_name, job_description in job_descriptions.items():

        # Empty description ko skip karna
        if not job_description.strip():
            continue

        # Text similarity score calculate karna
        text_score = calculate_match(
            resume_text,
            job_description
        )

        # Skills compare karna
        matched, missing, skill_score = compare_skills(resume_text,
            job_description
        )

        # Job ke results dictionary mein store karna
        results.append({
            "Job": job_name,
            "Text Similarity (%)": text_score,
            "Skill Match (%)": skill_score,
            "Matched Skills": ", ".join(matched),
            "Missing Skills": ", ".join(missing)
        })

    # Highest similarity score wali job ko pehle rakhna
    results.sort(
        key=lambda item: item["Text Similarity (%)"],
        reverse=True
    )

    # Final results return karna
    return results
