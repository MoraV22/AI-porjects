semantic_network: dict[str, dict[str, list[str]]] = {
    "James":{
        "is_a": ["Person"],
        "likes": ["Mona Lisa"],
        "is_in": [],
        "painted": []
    },
    "Mona Lisa":{
        "is_a": [],
        "likes": [],
        "is_in": ["Louvre"],
        "painted": []},
    "Louvre":{
        "is_a": ["Museum"],
        "likes": [],
        "is_in": ["Paris"],
        "painted": []},
        "Da Vinci":{
        "is_a": ["Person"],
        "likes": [],
        "is_in": [],
        "painted": ["Mona Lisa"]
        }
    }

def get_properties(concept : str) -> tuple[set[str], set[str], set[str]]:
    visited : set[str] = set()
    likes : set[str] = set()
    is_in : set[str] = set()
    painted : set[str] = set()

    def traverse(node : str):
        if node in visited:
            return
        visited.add(node)
        data = semantic_network.get(node, {})
        likes.update(data.get("likes", []))
        is_in.update(data.get("is_in", []))
        painted.update(data.get("painted", []))
        for parent in data.get("is_a", []):
            traverse(parent)

    traverse(concept)
    return likes, is_in, painted

def get_is_a(concept : str) -> set[str]:
    visited : set[str] = set()
    is_a : set[str] = set()

    def traverse(node : str):
        if node in visited:
            return
        visited.add(node)
        data = semantic_network.get(node, {})
        is_a.update(data.get("is_a", []))
        for parent in data.get("is_a", []):
            traverse(parent)

    traverse(concept)
    return is_a

def list_entities():
    """Convenience for UI dropdowns."""
    return sorted(semantic_network.keys())

