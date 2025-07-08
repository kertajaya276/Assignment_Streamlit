import streamlit as st 
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def tampilkan_analisis():
    tab1, tab2, tab3 = st.tabs(["Data", "Analisis", "Insight"])

    with tab1:
        st.header("Data Understanding")
        st.image("https://img.freepik.com/free-vector/customer-giving-quality-feedback_74855-5482.jpg", width=500)
        data = pd.read_csv("assignment_employee_survey.csv")
        st.write(data.head())

        with st.expander("Data Dictionary"):
            st.write('''
                    1. `emp_id` : Unique identifier for each employee.
                    2. `age`:  Age of the employee.
                    3. `gender`:  Gender of the employee (e.g., Male, Female, Other).
                    4. `marital_status`: Marital status of the employee (e.g., Single, Married, Divorced, Widowed)
                    5. `job_level` :  Job level of the employee (e.g., Intern/Fresher, Junior, Mid, Senior, Lead).
                    6. `experience` :  Number of years of work experience the employee has.
                    7. `dept` :  Department where the employee works (e.g., IT, HR, Finance, Marketing, Sales, Legal, Operations, Customer Service).
                    8. `emp_type`: Type of employment (e.g., Full-Time, Part-Time, Contract).
                    9. `wlb` : Work-life balance rating (scale from 1 to 5).
                    10. `work_env` : Work environment rating (scale from 1 to 5).
                    11. `physical_activity_hours` : Number of hours of physical activity per week.
                    12. `workload` : Workload rating (scale from 1 to 5).
                    13. `stress` : Stress level rating (scale from 1 to 5).
                    14. `sleep_hours` : Number of hours of sleep per night.
                    15. `commute_mode` : Mode of commute (e.g., Car, Public Transport, Bike, Walk, Motorbike).
                    16. `commute_distance` : Distance traveled during the commute (in kilometers).
                    17. `num_companies` : Number of different companies the employee has worked for.
                    18. `team_size` : Size of the team the employee is part of.
                    19. `num_report`: Number of people reported to by the employee (only applicable for Senior and Lead levels).
                    20. `edu_level` : Highest level of education achieved by the employee (e.g., High School, Bachelor, Master, PhD).
                    21. `have_ot` : Indicator if the employee has overtime (True/False).
                    22. `training_hours_per_year` : Number of hours of training received per year.
                    23. `job_satisfaction` : Rating of job satisfaction (scale from 1 to 5).
                    ''')
            
        with st.expander("Data Understanding"):
            st.write("""
                    1. Data berisi 23 kolom dan 2766 baris. 
                    2. Variabel utama yang menjadi analisis adalah gender, work life balance dan stress
                    3. Penelitian oleh Ganster & Rosen (2023) mengungkapkan bahwa stres kerja dapat menurunkan kepuasan kerja dan berdampak pada kesehatan karyawan .
                    4. Work-life balance memiliki pengaruh signifikan terhadap kepuasan kerja. Penelitian oleh Wahyu et al. (2021) menunjukkan bahwa work-life balance berpengaruh positif dan signifikan terhadap kepuasan kerja karyawan. Sehingga dalam analisis ini berfokus pada variabel-variabel tersebut.
                     """)
        
        with st.expander("Metode Pengolahan Data"):
            st.write("""
                    1. Dataset tidak memiliki nilai NULL dan tidak adanya missing value 
                    2. Data yang menjadi fokus yaitu work life balance (wlb) dan stress berupa skala 1-5
                    3. Job Satisfaction juga berupa skala 1-5
                    4. Analisis akan dilakukan melalui perbandingan antara Job satisfaction dengan variabel yang menjadi fokus.
                     """)

        
    
    with tab2:
        st.header("EDA")

        js_gender = data.groupby(['job_satisfaction', 'gender']).size().reset_index(name='count')

        st.subheader("Distribusi Job Satisfaction berdasarkan Gender ")

        # Plot dengan Plotly
        fig = px.bar(
                js_gender,
                x='job_satisfaction',
                y='count',
                color='gender',
                barmode='group',
                text='count',
                labels={'job_satisfaction': 'Job Satisfaction', 'count': 'Jumlah'},
                title='Distribusi Job Satisfaction berdasarkan Gender'
                    )

        # Styling
        fig.update_traces(textposition='outside')
        fig.update_layout(
                xaxis_title="Job Satisfaction",
                yaxis_title="Jumlah",
                legend_title="Gender",
                uniformtext_minsize=8,
                uniformtext_mode='hide'
        )

        # Tampilkan di Streamlit
        st.plotly_chart(fig, use_container_width=True)
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
            
    with tab3:
        st.header("Insight")
        st.write('''Dilihat dari visualisasi,  karyawan laki-laki dan wanita paling banyak memiliki kepuasan kerja yang baik dengan skala 4. 
                 Dari hasil ini dapat juga disimpulkan bahwa kesetaraan gender dalam perusahaan ini juga baik, sehingga disarankan untuk mempertahankan kebijakan perusahaan yang berkaitan dengan gender laki-laki dan wanita
                ''')
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

    

