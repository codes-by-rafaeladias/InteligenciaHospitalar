#Arquivo Transform: limpeza e preparação dos dados para análise 

def transform(df):
    '''
    inventario = pd.DataFrame({
    "variavel": df.columns,
    "valores_duplicados": df.duplicated().sum(),
    "valores_ausentes": df.isna().sum().values
    })
    
    print(inventario)
    

    print(df["A1Cresult"].value_counts(dropna=False))
    print(df["max_glu_serum"].value_counts(dropna=False))
    '''
    
    #1. Substituindo os valores ausentes dos exames por "Não registrado"
    df["A1Cresult"] = df["A1Cresult"].fillna("Not registered")
    df["max_glu_serum"] = df["max_glu_serum"].fillna("Not registered")
    
    
    '''
    #verificando quantidade de valores ausentes após preenchimento
    print(df[["A1Cresult", "max_glu_serum"]].isna().sum())
    
    #2. Verificando valores inválidos nas colunas numéricas
    print(df[df["time_in_hospital"] < 0].shape[0])
    print(df[df["num_lab_procedures"] < 0].shape[0])
    print(df[df["num_medications"] < 0].shape[0])
    print(df[df["number_outpatient"] < 0].shape[0])
    print(df[df["number_emergency"] < 0].shape[0])
    print(df[df["number_inpatient"] < 0].shape[0])
    print(df[df["num_procedures"] < 0].shape[0])
    print(df[df["number_diagnoses"] < 0].shape[0])
    '''
    
    #3. Substituindo Códigos/IDs por descrições de acordo com o arquivo utilitário
    admission_type = {
        1:"Emergency",
        2:"Urgent",
        3:"Elective",
        4:"Newborn",
        5:"Not Available",
        6: None,
        7:"Trauma Center",
        8:"Not Mapped"
    }
    
    discharge_disposition = {
        1:"Discharged to home",
        2:"Discharged/transferred to another short term hospital",
        3:"Discharged/transferred to SNF",
        4:"Discharged/transferred to ICF",
        5:"Discharged/transferred to another type of inpatient care institution",
        6:"Discharged/transferred to home with home health service",
        7:"Left AMA",
        8:"Discharged/transferred to home under care of Home IV provider",
        9:"Admitted as an inpatient to this hospital",
        10:"Neonate discharged to another hospital for neonatal aftercare",
        11:"Expired",
        12:"Still patient or expected to return for outpatient services",
        13:"Hospice / home",
        14:"Hospice / medical facility",
        15:"Discharged/transferred within this institution to Medicare approved swing bed",
        16:"Discharged/transferred/referred another institution for outpatient services",
        17:"Discharged/transferred/referred to this institution for outpatient services",
        18:None,
        19:"Expired at home. Medicaid only: hospice.",
        20:"Expired in a medical facility. Medicaid only: hospice.",
        21:"Expired: place unknown. Medicaid only: hospice.",
        22:"Discharged/transferred to another rehab fac including rehab units of a hospital .",
        23:"Discharged/transferred to a long term care hospital.",
        24:"Discharged/transferred to a nursing facility certified under Medicaid but not certified under Medicare.",
        25:"Not Mapped",
        26:"Unknown/Invalid",
        30:"Discharged/transferred to another Type of Health Care Institution not Defined Elsewhere",
        27:"Discharged/transferred to a federal health care facility.",
        28:"Discharged/transferred/referred to a psychiatric hospital of psychiatric distinct part unit of a hospital",
        29:"Discharged/transferred to a Critical Access Hospital (CAH)."
    }
    
    admission_source = {
        1: "Physician Referral",
        2: "Clinic Referral",
        3: "HMO Referral",
        4: "Transfer from a hospital",
        5: "Transfer from a Skilled Nursing Facility (SNF)",
        6: "Transfer from another health care facility",
        7: "Emergency Room",
        8: "Court/Law Enforcement",
        9: "Not Available",
        10: "Transfer from critial access hospital",
        11: "Normal Delivery",
        12: "Premature Delivery",
        13: "Sick Baby",
        14: "Extramural Birth",
        15: "Not Available",
        17: None,
        18: "Transfer From Another Home Health Agency",
        19: "Readmission to Same Home Health Agency",
        20: "Not Mapped",
        21: "Unknown/Invalid",
        22: "Transfer from hospital inpt/same fac reslt in a sep claim",
        23: "Born inside this hospital",
        24: "Born outside this hospital",
        25: "Transfer from Ambulatory Surgery Center",
        26: "Transfer from Hospice",
    }
    
    df["admission_type_id"] = (df["admission_type_id"].map(admission_type))
    df["discharge_disposition_id"] = (df["discharge_disposition_id"].map(discharge_disposition))
    df["admission_source_id"] = (df["admission_source_id"].map(admission_source))
    
    '''
    #verificando valores ausentes
    print(df["admission_type_id"].value_counts(dropna=False))
    print(df["discharge_disposition_id"].value_counts(dropna=False))
    print(df["admission_source_id"].value_counts(dropna=False))
    '''
    
    #substituindo os valores ausentes por "Não especificado"
    df["admission_type_id"] = df["admission_type_id"].fillna("Not specified")
    df["discharge_disposition_id"] = df["discharge_disposition_id"].fillna("Not specified")
    df["admission_source_id"] = df["admission_source_id"].fillna("Not specified")
    
    '''
    #verificando quantidade de valores ausentes após preenchimento
    print(df[["admission_type_id", "discharge_disposition_id", "admission_source_id" ]].isna().sum())
    '''
    
    #4. Renomeando as principais colunas que serão utilizadas para análise
    df = df.rename(columns={
    "encounter_id": "id_internacao",
    "patient_nbr": "id_paciente",
    "time_in_hospital": "tempo_internacao",
    "num_lab_procedures": "qtd_exames_laboratoriais",
    "num_medications": "qtd_medicamentos",
    "race": "raca",
    "gender": "genero",
    "weight": "peso",
    "admission_type_id": "tipo_internacao",
    "discharge_disposition_id": "destino_internacao",
    "admission_source_id": "origem_internacao",
    "A1Cresult": "hbA1c_resultado",
    "diabetesMed": "uso_medicamento_diabetes",
    "readmitted": "readmissao"
    })
    
    #verificando se as colunas foram renomeadas
    '''
    print(df.columns.tolist())
    '''
    
    return df