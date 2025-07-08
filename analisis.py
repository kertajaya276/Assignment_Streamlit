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

        
        fig.update_traces(textposition='outside')
        fig.update_layout(
                xaxis_title="Job Satisfaction",
                yaxis_title="Jumlah",
                legend_title="Gender",
                uniformtext_minsize=8,
                uniformtext_mode='hide'
        )

        st.plotly_chart(fig, use_container_width=True,  key="plot_gender")


        ###
        st.sidebar.header("Filter Data")

        # Dropdown Work Life Balance
        wlb_options = sorted(data['wlb'].dropna().unique())
        selected_wlb = st.sidebar.multiselect("Work Life Balance", options=wlb_options, default=wlb_options)

        # Dropdown Job Satisfaction
        js_options = sorted(data['job_satisfaction'].dropna().unique())
        selected_js = st.sidebar.multiselect("Job Satisfaction", options=js_options, default=js_options)

        # --- Filter Data ---
        filtered_data = data[
            data['wlb'].isin(selected_wlb) &
            data['job_satisfaction'].isin(selected_js)
        ]

        # --- Grouped Data ---
        js_wlb = filtered_data.groupby(['wlb', 'job_satisfaction']).size().reset_index(name='count')

        # --- Plot ---
        st.subheader(" Distribusi Job Satisfaction berdasarkan Work Life Balance")

        if js_wlb.empty:
            st.warning("Data tidak ditemukan untuk kombinasi filter tersebut.")
        else:
            fig = px.bar(
                js_wlb,
                x='wlb',
                y='count',
                color='job_satisfaction',
                barmode='group',
                text='count',
                labels={
                    'wlb': 'Work Life Balance',
                    'count': 'Jumlah Karyawan',
                    'job_satisfaction': 'Job Satisfaction'
                },
                title='Distribusi Job Satisfaction berdasarkan Work Life Balance'
            )

            fig.update_traces(textposition='outside')
            fig.update_layout(
                xaxis_title="Work Life Balance",
                yaxis_title="Jumlah Karyawan",
                legend_title="Job Satisfaction",
                uniformtext_minsize=8,
                uniformtext_mode='hide'
            )

        st.plotly_chart(fig, use_container_width=True, key="plot_wlb")

        ### Sidebar Filters
        st.sidebar.header("Filter Data")

        # Filter job satisfaction
        js_options = sorted(data['job_satisfaction'].dropna().unique())
        selected_js_stress = st.sidebar.multiselect("Job Satisfaction", options=js_options, default=js_options, key="js_stress")

        # Filter stress range
        stress_min, stress_max = int(data['stress'].min()), int(data['stress'].max())
        selected_stress = st.sidebar.slider("Rentang Stress", stress_min, stress_max, (stress_min, stress_max))

        # Filter data
        filtered_df = data[
            (data['job_satisfaction'].isin(selected_js)) &
            (data['stress'] >= selected_stress[0]) &
            (data['stress'] <= selected_stress[1])
        ]

        # Crosstab dengan jumlah unik emp_id
        js_stress = pd.crosstab(
            index=filtered_df['stress'],
            columns=filtered_df['job_satisfaction'],
            values=filtered_df['emp_id'],
            aggfunc='nunique'
        )

        # Jika kolomnya kosong setelah filter
        if js_stress.empty:
            st.subheader("Distribusi Job Satisfaction berdasarkan Stress")
            st.warning("Data tidak ditemukan untuk kombinasi filter tersebut.")
        else:
            # Ubah format ke long agar bisa di-plot
            js_stress = js_stress.reset_index().melt(id_vars='stress', var_name='job_satisfaction', value_name='count')

            st.subheader("Distribusi Job Satisfaction berdasarkan Stress")

            # Plot
            fig = px.bar(
                js_stress,
                x='stress',
                y='count',
                color='job_satisfaction',
                barmode='group',
                text='count',
                labels={
                    'stress': 'Stress',
                    'count': 'Jumlah Karyawan',
                    'job_satisfaction': 'Job Satisfaction'
                },
                title='Distribusi Job Satisfaction berdasarkan Stress'
            )

            fig.update_traces(textposition='outside')
            fig.update_layout(
                xaxis_title="Stress",
                yaxis_title="Jumlah Karyawan",
                legend_title="Job Satisfaction",
                uniformtext_minsize=8,
                uniformtext_mode='hide'
            )

            st.plotly_chart(fig, use_container_width=True, key="plot_stress")  




    with tab3:
        st.header("Insight")
        st.subheader("Distribusi Job Satisfaction berdasarkan Gender ")
        st.image('gender.png')
        st.write('''Dilihat dari visualisasi,  karyawan laki-laki dan wanita paling banyak memiliki kepuasan kerja yang baik dengan skala 4. 
                 Dari hasil ini dapat juga disimpulkan bahwa kesetaraan gender dalam perusahaan ini juga baik, sehingga disarankan untuk mempertahankan kebijakan perusahaan yang berkaitan dengan gender laki-laki dan wanita
                ''')
        
        st.subheader("Distribusi Job Satisfaction berdasarkan Work Life Balance")
        st.image('wlb.png')
        st.write('''
                Dapat diketahui bahwa work life balance sangat mempengaruhi kepuasan kerja, yang mana work life balance skala 5 (sangat baik) memiliki kepuasan kerja yang baik pula dengan skala 4.
                 Disarankan perusahaan lebih memperhatikan kehidupan karyawan dengan cara, tidak memberi banyak lembur atau memberi upah lembur,  memberi tunjangan kepada karyawan yang menikah,  dan lain sebagainya.
                ''')
        
        st.subheader("Distribusi Job Satisfaction berdasarkan tingkat stress")
        st.image('stress.png')
        st.write('''
                Dilihat dari visualisasi, tingkat stress karyawan memiliki pengaruh terhadap kepuasan kerja.
                Secara garis besar karyawan memiliki tingkat stress yang rendah.
                 Karyawan dengan tingkat stress yang rendah yaitu skala 1 memiliki kepuasan kerja yang baik dengan skala 4 paling banyak dengan jumlah 760 orang.
                 Dari hasil ini dapat juga disarankan agar perusahaan memerhatikan karyawan tingkat stress rendah dengan kepuasan kerja rendah pula, karena kemungkinan adanya faktor lain yang memengaruhi kepuasan kerja.
                    ''')
    
    

