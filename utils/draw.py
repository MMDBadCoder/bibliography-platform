import matplotlib.pyplot as plt
import networkx as nx


def draw_citation_graph(articles):
    # Create a directed graph
    G = nx.DiGraph()

    # Create a mapping from article titles to WOS IDs
    title_to_wos_id = {}

    for article in articles:
        title = article.get('Title', 'Untitled')
        wos_id = article.get('WOS_ID', 'Unknown ID')
        title_to_wos_id[title] = wos_id  # Map title to WOS ID
        G.add_node(wos_id, title=title)  # Add node to the graph

    # Create citation relationships (edges)
    for article in articles:
        wos_id = article.get('WOS_ID', 'Unknown ID')
        cited_references = article.get('CitedReferences', [])

        for cited_ref in cited_references:
            # Attempt to get the WOS ID from the title using the map
            cited_id = title_to_wos_id.get(cited_ref)

            if cited_id:
                # Add a directed edge from the citing article to the cited article
                G.add_edge(wos_id, cited_id)

    # Visualize the graph
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G)  # Position nodes using Fruchterman-Reingold force-directed algorithm
    nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, node_color='lightblue', font_color='black',
            arrows=True)
    plt.title('Citation Network of Articles')
    plt.show()
