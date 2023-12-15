import file_preparation as fp
import networkx as nx
import matplotlib.pyplot as plt

students = fp.studants_dict
projects = fp.projects_requirements_dict

def gale_shapley(preferences_students, projects):
    # Inicializar projetos e alunos disponíveis
    projects_available = set(projects.keys())
    students_available = set(preferences_students.keys())

    # Dicionário para armazenar os emparelhamentos (projeto: aluno)
    pairings = {}

    # Loop para 10 iterações
    for iteration in range(10):
        # Enquanto houver projetos disponíveis
        while projects_available:
            project = projects_available.pop()
            vacancies_available, grade_cutoff = projects[project]

            # Encontrar alunos que preferem o projeto atual e atendem à nota de corte
            preferred_students = preferences_students.keys()
            preferred_students = [student for student in preferred_students if project in preferences_students[student][:3] and preferences_students[student][3] >= grade_cutoff]

            # Ordenar alunos preferidos com base na nota e preferência
            preferred_students.sort(key=lambda student: (preferences_students[student][3], preferences_students[student].index(project)))

            # Emparelhar alunos ao projeto
            for student in preferred_students:
                if student not in pairings:
                    pairings[student] = project
                    break
                else:
                    current_project = pairings[student]
                    if preferences_students[student].index(project) < preferences_students[student].index(current_project):
                        pairings[student] = project
                        projects_available.add(current_project)
                        break

        # Mostrar resultados após cada iteração
        print(f"\nIteração {iteration + 1} - Pares Projetos x Alunos:")
        for student, project in pairings.items():
            print(f"Aluno {student} está associado ao projeto {project}")

    return pairings
def visualize_bipartite_graph(preferences_students, projects, pairings):
    # Criar um grafo bipartido
    G = nx.Graph()

    # Adicionar nós do lado dos alunos e projetos
    G.add_nodes_from(preferences_students.keys(), bipartite=0)
    G.add_nodes_from(projects.keys(), bipartite=1)

    # Adicionar arestas entre alunos e projetos pareados
    for student, project in pairings.items():
        G.add_edge(student, project)

    # Identificar os nós conectados ao remover os nós não conectados
    connected_nodes = set(pairings.keys()).union(set(pairings.values()))
    G.remove_nodes_from([node for node in G.nodes if node not in connected_nodes])

    # Posicionamento dos nós para visualização
    pos_students = {node: (1, i) for i, node in enumerate(preferences_students.keys())}
    pos_projects = {node: (2, i) for i, node in enumerate(projects.keys())}
    pos = {**pos_students, **pos_projects}

    # Desenhar o grafo bipartido
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    plt.show()
# Exemplo de uso:
# Supondo que você tenha as variáveis students, projects, e result definidas
# no seu ambiente de trabalho.


# Exemplo de uso
result = gale_shapley(students, projects)
visualize_bipartite_graph(students, projects, result)

print("\nResultado Final - Pares Projetos x Alunos:")
for student, project in result.items():
    print(f"Aluno {student} está associado ao projeto {project}")
