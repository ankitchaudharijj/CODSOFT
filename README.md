
# 🎬 Movie Recommendation System

This is a simple **Content-Based Movie Recommendation System** built using Python. It suggests movies based on genres using TF-IDF and cosine similarity.

## 📁 Files Included
- `recommendation.py` - Main Python script for the recommender.
- `movies.csv` - Sample dataset of 10 Marvel movies with genres.
- `Movie_Recommendation_Report.pdf` - Report with explanation & sample output.
- `README.md` - This file.

## 🚀 How It Works
1. **TF-IDF Vectorization**: Converts genres into numerical vectors.
2. **Cosine Similarity**: Measures similarity between movies based on genre.
3. **Recommendation**: Returns the top similar movies to the input.

## 📦 Requirements
- Python 3.x
- pandas
- scikit-learn

Install the required libraries with:
```bash
pip install pandas scikit-learn
```

## ▶️ How to Run
```bash
python recommendation.py
```

The script will print recommended movies similar to "Iron Man".

## 🧠 Example Output
```
Movies similar to 'Iron Man':
The Avengers
Captain America: The First Avenger
Guardians of the Galaxy
Black Panther
Spider-Man: Homecoming
```

## 📌 Notes
- This project uses a very small dataset for demo purposes.
- Can be enhanced using collaborative filtering or larger datasets like MovieLens.

## 👨‍💻 Author
**Ankit Chaudhari**  
Delhi Skill and Entrepreneurship University  
GitHub: [ankitchaudharijj](https://github.com/ankitchaudharijj)  
LinkedIn: [Ankit Chaudhari](https://www.linkedin.com/in/ankit-chaudhari-40346b318/)
