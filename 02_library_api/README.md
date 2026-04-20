<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=009688&center=true&vCenter=true&width=900&lines=FastAPI+Book+Management+System;High-Performance+RESTful+API;FastAPI+%7C+SQLAlchemy+%7C+Pydantic;Modern+Backend+Architecture" />

<p>
  <a href="https://www.linkedin.com/in/mohammed-manzar-maaz">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.10+-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlite&logoColor=white" />
</p>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=009688" width="100%" />

</div>

<h2 align="center">⚡ Overview</h2>

<p align="center">
  <b>How do you build a lightning-fast, production-ready API with automatic documentation?</b><br>
  I developed a scalable <b>Book Management API</b> utilizing modern Python backend technologies to handle asynchronous routing, strict data validation, and relational database management.
</p>

<p align="center">
  This project explores:<br>
  🚀 <b>Speed & Concurrency:</b> Leveraging FastAPI's ASGI foundation for high performance.<br>
  🛡️ <b>Data Validation:</b> Utilizing Pydantic schemas to ensure data integrity before it hits the database.<br>
  🗄️ <b>ORM Integration:</b> Managing relational models and session lifecycles with SQLAlchemy.
</p>

<br>

<h2 align="center">⚙️ Tech Stack & Tools</h2>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,postgres,sqlite" />
</p>

<table align="center">
  <tr>
    <th>Category</th>
    <th>Technologies Used</th>
  </tr>
  <tr>
    <td align="center"><b>Framework</b></td>
    <td align="center"><img src="https://img.shields.io/badge/FastAPI-High%20Performance-009688?style=flat-square&logo=fastapi" /></td>
  </tr>
  <tr>
    <td align="center"><b>Database / ORM</b></td>
    <td align="center"><img src="https://img.shields.io/badge/SQLAlchemy-Object%20Relational%20Mapper-red?style=flat-square&logo=databricks" /></td>
  </tr>
  <tr>
    <td align="center"><b>Validation</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Pydantic-Data%20Parsing-blue?style=flat-square&logo=python" /></td>
  </tr>
  <tr>
    <td align="center"><b>Server</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Uvicorn-ASGI%20Server-orange?style=flat-square" /></td>
  </tr>
</table>

<br>

<h2 align="center">🧠 Architecture & Engineering Decisions</h2>

<p align="center">
  Separation of concerns is critical for a maintainable backend. This API strictly divides routing, data validation, and database operations.
</p>

### 🔧 Key Techniques Used

- **Dependency Injection:** Database sessions are yielded using FastAPI's `Depends()`, ensuring connections are safely opened and closed per request.
- **Schema vs. Model Separation:** Prevented over-posting vulnerabilities by using `BookCreate` (Pydantic) for incoming requests and mapping it to `Book` (SQLAlchemy) for database storage.
- **Environment Variables:** Secured database connection strings using `python-dotenv` to keep credentials out of version control.
- **Automatic Interactive Docs:** Configured to automatically generate Swagger UI and ReDoc interfaces.

<br>

<h2 align="center">🛣️ API Endpoints</h2>

| Method | Endpoint | Description | Request Body | Response |
|:---|:---|:---|:---|:---|
| `POST` | `/books/` | Creates a new book entry in the database. | `{"title": "...", "author": "...", "rating": 4.5}` | `200 OK` |
| `GET` | `/books/` | Retrieves a list of all books. | *None* | `200 OK` |

<br>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=009688" width="100%" />

<h2 align="center">🚀 Getting Started</h2>

**1. Clone the repository**

```bash
git clone https://github.com/YourUsername/fastapi-book-api.git
cd fastapi-book-api
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install fastapi uvicorn sqlalchemy pydantic python-dotenv
```

**4. Set up environment variables**

Create a `.env` file in the root directory:

```env
DATABASE_URL="sqlite:///./books.db"
```

**5. Launch the server**

```bash
uvicorn main:app --reload
```

Navigate to `http://127.0.0.1:8000/docs` to interact with the Swagger UI.

<div align="center">
  <h3>👤 Author: Mohammed Manzar Maaz</h3>
  <p>
    <a href="https://www.linkedin.com/in/mohammed-manzar-maaz">
      <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" />
    </a>
    <a href="https://github.com/ManzarMaaz">
      <img src="https://img.shields.io/github/followers/ManzarMaaz?label=Follow&style=social" />
    </a>
  </p>
</div>
