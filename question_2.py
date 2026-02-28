import numpy as np
from sklearn.neighbors import NearestNeighbors

case_base: list[dict[str, int | str]] = [
    {"cv": 1500, "brand": "Toyota", "mileage": 50000, "mile gallon rate": 30, "color": "red", "price": 15000, "model": "Corolla"},
    {"cv": 1200, "brand": "Honda", "mileage": 75000, "mile gallon rate": 28, "color": "blue", "price": 12000, "model": "Civic"},
    {"cv": 1800, "brand": "Ford", "mileage": 30000, "mile gallon rate": 25, "color": "black", "price": 18000, "model": "Focus"},
    {"cv": 2000, "brand": "BMW", "mileage": 40000, "mile gallon rate": 22, "color": "white", "price": 25000, "model": "3 Series"},
    {"cv": 1600, "brand": "Hyundai", "mileage": 60000, "mile gallon rate": 29, "color": "silver", "price": 14000, "model": "Elantra"},
    {"cv": 2200, "brand": "Mercedes", "mileage": 25000, "mile gallon rate": 20, "color": "gray", "price": 30000, "model": "C-Class"},
    {"cv": 1400, "brand": "Mazda", "mileage": 55000, "mile gallon rate": 31, "color": "green", "price": 13500, "model": "3"},
    {"cv": 1900, "brand": "Audi", "mileage": 45000, "mile gallon rate": 23, "color": "brown", "price": 27000, "model": "A4"},
    {"cv": 1300, "brand": "Kia", "mileage": 80000, "mile gallon rate": 27, "color": "orange", "price": 11500, "model": "Forte"},
    {"cv": 2100, "brand": "Volkswagen", "mileage": 35000, "mile gallon rate": 24, "color": "purple", "price": 22000, "model": "Jetta"},
    {"cv": 1550, "brand": "Nissan", "mileage": 65000, "mile gallon rate": 26, "color": "yellow", "price": 16000, "model": "Altima"},
]


def _build_mappings() -> tuple[dict[str |int, int], dict[str|int, int]]:
    brands = sorted({c["brand"] for c in case_base})
    colors = sorted({c["color"] for c in case_base})
    brand_mapping = {b: i for i, b in enumerate(brands)}
    color_mapping = {c: i for i, c in enumerate(colors)}
    return brand_mapping, color_mapping


def encode_case(case: dict[str, int | str]) -> np.ndarray:
    """
    Encodes a car case to a numeric vector: [cv, brand_id, mileage, mpg, color_id, price]
    """
    brand_mapping, color_mapping = _build_mappings()

    return np.array(
        [
            case["cv"],
            brand_mapping[case["brand"]],
            case["mileage"],
            case["mile gallon rate"],
            color_mapping[case["color"]],
            case["price"],
        ],
        dtype=float,
    )


def list_brands():
    return sorted({c["brand"] for c in case_base})


def list_colors():
    return sorted({c["color"] for c in case_base})


def find_best_matches(new_case: dict[str, int | str], k: int = 3) -> list[dict[str, int | dict[str,int|str]]]:
    """
    Case-Based Reasoning: returns the k most similar cases (nearest neighbors).
    Output: list of dicts {distance, index, case}
    """
    X: np.ndarray = np.vstack([encode_case(c, ) for c in case_base])
    x_new: np.ndarray = encode_case(new_case).reshape(1, -1)

    k = max(1, min(int(k), len(case_base)))
    nn = NearestNeighbors(n_neighbors=k, metric="euclidean")
    nn.fit(X)

    distances, indices = nn.kneighbors(x_new)

    results = []
    for d, i in zip(distances[0], indices[0]):
        results.append({"distance": float(d), "index": int(i), "case": case_base[int(i)]})
    return results

