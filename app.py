# Required libraries import karna
import streamlit as st
import pandas as pd

# Apni project files se functions import karna
from resume_parser import extract_resume_text
from job_comparator import compare_jobs

# Website ka page setup
st.set_page_config(
    page_title="Smart Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Website ka title aur introduction
st.title("Smart Resume–Job Matching Analyzer")

st.write(
    "Upload your resume and compare it with job descriptions "
    "to find matching skills and missing skills."
)

st.divider()

# Sidebar mein project information
st.sidebar.title("About Project")

st.sidebar.write(
    "This project analyzes a resume and compares it "
    "with different job descriptions."
)

# Step 1: Resume PDF upload karna
st.header("Step 1: Upload Your Resume")

uploaded_file = st.file_uploader(
    "Select your resume PDF",
    type=["pdf"]
)

# Step 2: Job descriptions enter karna
st.header("Step 2: Enter Job Descriptions")

job1 = st.text_area(
    "Job 1 Description",
    placeholder="Enter the first job description here..."
)

job2 = st.text_area(
    "Job 2 Description",
    placeholder="Enter the second job description here..."
)

job3 = st.text_area(
    "Job 3 Description",
    placeholder="Enter the third job description here..."
)

# Resume analyze karne ka button
if st.button("Analyze Resume"):

    # Check karna ki resume upload hua hai
    if uploaded_file is None:
        st.error("Please upload your resume PDF.")

    # Check karna ki job description enter ki gayi hai
    elif not any([job1.strip(), job2.strip(), job3.strip()]):
        st.error("Please enter at least one job description.")

    else:
        try:
            # Resume PDF se text extract karna
            resume_text = extract_resume_text(uploaded_file)

            # Check karna ki PDF mein readable text hai
            if not resume_text.strip():
                st.error(
                    "No readable text found in the PDF. "
                    "Please upload a text-based resume."
                )

            else:
                # Job descriptions ko dictionary mein store karna
                job_descriptions = {
                    "Job 1": job1,
                    "Job 2": job2,
                    "Job 3": job3
                }

                # Resume ko sabhi jobs ke saath compare karna
                results = compare_jobs(
                    resume_text,
                    job_descriptions
                )

                # Agar results nahi mile
                if not results:
                    st.warning(
                        "Please enter a valid job description."
                    )

                else:
                    # Results ko table mein convert karna
                    df = pd.DataFrame(results)

                    # Analysis results show karna
                    st.header("Step 3: Analysis Results")

                    st.dataframe(
                        df,
                        use_container_width=True,
                        hide_index=True
                    )

                    # Best text similarity wala job show karna
                    best_job = results[0]

                    st.subheader("Best Matching Job")

                    st.success(
                        f"{best_job['Job']} - "
                        f"{best_job['Text Similarity (%)']}% "
                        "text similarity"
                    )

                    # Har job ki skills details show karna
                    st.header("Skills Analysis")

                    for result in results:

                        with st.expander(result["Job"]):

                            st.write(
                                "Text Similarity:",
                                str(
                                    result["Text Similarity (%)"]
                                ) + "%"
                            )

                            st.write(
                                "Skill Match:",
                                str(
                                    result["Skill Match (%)"]
                                ) + "%"
                            )

                            st.write(
                                "Matched Skills:",
                                result["Matched Skills"]
                                if result["Matched Skills"]
                                else "No matched skills found."
                            )

                            st.write(
                                "Missing Skills:",
                                result["Missing Skills"]
                                if result["Missing Skills"]
                                else "No missing skills from the checked list."
                            )

                    # Job comparison chart show karna
                    st.header("Job Comparison Chart")

                    chart_data = df.set_index("Job")[
                        [
                            "Text Similarity (%)",
                            "Skill Match (%)"
                        ]
                    ]

                    st.bar_chart(chart_data)

                    # Analysis results ko CSV format mein convert karna
                    csv_data = df.to_csv(
                        index=False
                    ).encode("utf-8")

                    # Report download button
                    st.download_button(
                        label="Download Analysis Report",
                        data=csv_data,
                        file_name="resume_analysis_report.csv",
                        mime="text/csv"
                    )

        # Agar analysis mein error aaye toh message show karna
        except Exception as error:
            st.error("An error occurred during analysis.")
            st.write(str(error))

# Website ke bottom mein note
st.divider()

st.caption(
    "Note: Matching scores are estimates and do not "
    "guarantee job selection."
)
