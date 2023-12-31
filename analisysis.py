from owlready2 import *
import matplotlib.pyplot as plt
import numpy as np

onto = get_ontology("ontologyCompleted.rdf").load()

# Consulta SPARQL para obter a quantidade de alunos com desempenho acadêmico excelente
studentsForStatus = list(default_world.sparql("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ont: <http://www.semanticweb.org/jo_az/ontologies/2023/10/untitled-ontology-14#>

SELECT ?subclasse (COUNT(?student) AS ?count)
WHERE {
  ?student rdf:type ont:Student.

  ?student ont:StudentHasStatus ?status.
  ?status rdf:type ?subclasse.
  ?subclasse rdfs:subClassOf ont:Status.
}
GROUP BY ?subclasse
"""))



StudentsForEthnicity = list(default_world.sparql("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ont: <http://www.semanticweb.org/jo_az/ontologies/2023/10/untitled-ontology-14#>

SELECT ?subclasse (COUNT(?student) AS ?count)
WHERE {
  ?student rdf:type ont:Student.

  ?student ont:StudentHasEthnicity ?eth.
  ?eth rdf:type ?subclasse.
  ?subclasse rdfs:subClassOf ont:Ethnicity.
}
GROUP BY ?subclasse
"""))


StudentsForGenrer = list(default_world.sparql("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ont: <http://www.semanticweb.org/jo_az/ontologies/2023/10/untitled-ontology-14#>

SELECT ?subclasse (COUNT(?student) AS ?count)
WHERE {
  ?student rdf:type ont:Student.

  ?student ont:StudentHasGender ?gender.
  ?gender rdf:type ?subclasse.
  ?subclasse rdfs:subClassOf ont:Gender.
}
GROUP BY ?subclasse
"""))

StudentsReceivedST = list(default_world.sparql("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ont: <http://www.semanticweb.org/jo_az/ontologies/2023/10/untitled-ontology-14#>

SELECT ?subclasse (COUNT(?student) AS ?count)
WHERE {
  ?student rdf:type ont:Student.

  ?student ont:StudentReceivedStudentAssistance ?assistance.
  ?assistance rdf:type ?subclasse.
  ?subclasse rdfs:subClassOf ont:StudentAssistance.
}
GROUP BY ?subclasse
"""))



StudentsWithDrawnForPerformance = list(default_world.sparql("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ont: <http://www.semanticweb.org/jo_az/ontologies/2023/10/untitled-ontology-14#>

SELECT ?subclasse (COUNT(?student) AS ?count)
WHERE {
  ?student rdf:type ont:Student.
  ?student ont:StudentHasStatus ?status.
  ?status rdf:type ont:Withdrawn.

  ?student ont:StudentHasAcademicPerformance ?performance.
  ?performance rdf:type ?subclasse.
  ?subclasse rdfs:subClassOf ont:AcademicPerformance.
}
GROUP BY ?subclasse
"""))


StudentsCompletedForPerformance = list(default_world.sparql("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ont: <http://www.semanticweb.org/jo_az/ontologies/2023/10/untitled-ontology-14#>

SELECT ?subclasse (COUNT(?student) AS ?count)
WHERE {
  ?student rdf:type ont:Student.
  ?student ont:StudentHasStatus ?status.
  ?status rdf:type ont:Completed.

  ?student ont:StudentHasAcademicPerformance ?performance.
  ?performance rdf:type ?subclasse.
  ?subclasse rdfs:subClassOf ont:AcademicPerformance.
}
GROUP BY ?subclasse
"""))


StudentsDropOutForPeriod = list(default_world.sparql("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ont: <http://www.semanticweb.org/jo_az/ontologies/2023/10/untitled-ontology-14#>

SELECT ?subclasse (COUNT(?student) AS ?count)
WHERE {
  ?student rdf:type ont:Student.
  ?student ont:StudentHasStatus ?status.
  ?status rdf:type ont:Withdrawn.

  ?student ont:StudentDroppedOutInPeriod ?drop.
  ?drop rdf:type ?subclasse.
  ?subclasse rdfs:subClassOf ont:PeriodDropout.
}
GROUP BY ?subclasse
"""))



StudentsNotReceivedSTAndCompletedWithdrown = list(default_world.sparql("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ont: <http://www.semanticweb.org/jo_az/ontologies/2023/10/untitled-ontology-14#>

SELECT ?subclasse (COUNT(?student) AS ?count)
WHERE {
  ?student rdf:type ont:Student.
  ?student ont:StudentReceivedStudentAssistance ?assistance.
  ?assistance rdf:type ont:NotReceived.                                        
  ?student ont:StudentHasStatus ?status.
  ?status rdf:type ?subclasse.
  ?subclasse rdfs:subClassOf ont:Status.
                                                                    
  FILTER (?subclasse = ont:Completed || ?subclasse = ont:Withdrawn)  # Filter for 'Completed' or 'Withdrawn' subclasses

}
GROUP BY ?subclasse
"""))


StudentsReceivedSTAndCompletedWithdrown = list(default_world.sparql("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ont: <http://www.semanticweb.org/jo_az/ontologies/2023/10/untitled-ontology-14#>

SELECT ?subclasse (COUNT(?student) AS ?count)
WHERE {
  ?student rdf:type ont:Student.
  ?student ont:StudentReceivedStudentAssistance ?assistance.
  ?assistance rdf:type ont:Received.                                        
  ?student ont:StudentHasStatus ?status.
  ?status rdf:type ?subclasse.
  ?subclasse rdfs:subClassOf ont:Status.
                                                                    
  FILTER (?subclasse = ont:Completed || ?subclasse = ont:Withdrawn)  # Filter for 'Completed' or 'Withdrawn' subclasses

}
GROUP BY ?subclasse
"""))


StudentsQuotaStatus = list(default_world.sparql("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ont: <http://www.semanticweb.org/jo_az/ontologies/2023/10/untitled-ontology-14#>

SELECT ?subclasse (COUNT(?student) AS ?count)
WHERE {
  ?student rdf:type ont:Student.
  ?student ont:StudentHasAdmissionType ?adm.
  ?adm rdf:type ont:Quota. 
                                                
  ?student ont:StudentHasStatus?status.
  ?status rdf:type ?subclasse.
  ?subclasse rdfs:subClassOf ont:Status.
  FILTER (?subclasse = ont:Completed || ?subclasse = ont:Withdrawn)  # Filter for 'Completed' or 'Withdrawn' subclasses
}
GROUP BY ?subclasse
"""))


StudentsNonQuotaStatus = list(default_world.sparql("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ont: <http://www.semanticweb.org/jo_az/ontologies/2023/10/untitled-ontology-14#>

SELECT ?subclasse (COUNT(?student) AS ?count)
WHERE {
  ?student rdf:type ont:Student.
  ?student ont:StudentHasAdmissionType ?adm.
  ?adm rdf:type ont:NonQuota. 
                                                
  ?student ont:StudentHasStatus?status.
  ?status rdf:type ?subclasse.
  ?subclasse rdfs:subClassOf ont:Status.
  FILTER (?subclasse = ont:Completed || ?subclasse = ont:Withdrawn)  # Filter for 'Completed' or 'Withdrawn' subclasses
}
GROUP BY ?subclasse
"""))


import matplotlib.pyplot as plt
import numpy as np

# Função para gerar gráficos de pizza a partir dos resultados da consulta SPARQL
def generate_pie_chart(results, title):
    labels, values = zip(*results)
    
    labels= np.array(labels)
    labels_arr = []
    for label in labels:
        labels_aux = str(label)
        if('.' in labels_aux):
          labels_aux = labels_aux.split(".")[1]
          labels_arr.append(labels_aux)
        else:
          labels_arr.append(labels_aux)
   
    # Convertendo os valores para numpy arrays para facilitar o uso com o matplotlib
    values = np.array(values)
    print(labels_aux)
     
    
    # Criando um gráfico de pizza
    plt.pie(values, labels=labels_arr, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

# Gerando gráficos de pizza para cada consulta SPARQL
generate_pie_chart(StudentsQuotaStatus , "Quota Students by Status")
generate_pie_chart(StudentsNonQuotaStatus , "Non-Quota Students by Status")
generate_pie_chart(StudentsNotReceivedSTAndCompletedWithdrown , "Students who did not receive student assistance")
generate_pie_chart(StudentsReceivedSTAndCompletedWithdrown , "Students who received student assistance.")
generate_pie_chart(studentsForStatus, "Distribution of Students by Status")
generate_pie_chart(StudentsForEthnicity, "Distribution of Students by Ethnicity")
generate_pie_chart(StudentsForGenrer, "Distribution of Students by Gender")
generate_pie_chart(StudentsReceivedST, "Distribution of Students who Received Student Assistance")
generate_pie_chart(StudentsWithDrawnForPerformance, "Academic Performance of Withdrawn Students")
generate_pie_chart(StudentsCompletedForPerformance, "Academic Performance of Completed Students")
generate_pie_chart(StudentsDropOutForPeriod, "Students who Dropped Out in a Period")







    
