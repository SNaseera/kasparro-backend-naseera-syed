**Kasparro Backend & ETL Systems Assignment**

**Candidate:** Naseera Kouser Syed
**Track:** Backend & ETL Systems
**Repository:** kasparro-backend-naseera-kouser

---

**_Project Overview_**

This project is a production-style backend service with an ETL (Extract–Transform–Load) pipeline, built as part of the Kasparro Backend & ETL Systems Assignment.

It demonstrates:
- Clean backend architecture using FastAPI  
- Structured ETL pipeline design  
- Modular folder organization  
- Database persistence using SQLAlchemy  
- Docker-ready deployment  
- Clean coding practices suitable for real-world systems

The system simulates ingestion of structured data, applies transformations, and persists it into a relational database with API access.

---

**System Architecture**

<img width="1024" height="1536" alt="ChatGPT Image Dec 9, 2025, 11_41_32 AM" src="https://github.com/user-attachments/assets/dc4e34c0-77dc-4492-a243-6e305af0a70b" />

---

**Folder Structure**

kasparro-backend-naseera-syed/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI entry point
│   ├── models.py               # Database models
│   ├── schemas.py              # Pydantic schemas
│   ├── crud.py                 # DB operations
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── routes.py       # API routes
│   │       └── deps.py         # Dependencies
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── session.py
│   └── etl/
│       ├── __init__.py
│       ├── ingest.py
│       ├── transform.py
│       ├── load.py
│       └── crypto_api.py       # CoinPaprika & CoinGecko integration
├── scripts/
│   └── run_etl.py              # ETL runner script
├── tests/
│   └── test_api.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
├── alembic.ini
└── README.md

---

**Technology Stack**

| Layer              | Technology             |
| ------------------ | ---------------------- |
| Backend API        | FastAPI                |
| ORM                | SQLAlchemy             |
| Database           | SQLite                 |
| ETL                | Custom Python Pipeline |
| Testing            | Pytest                 |
| Containerization   | Docker                 |
| Environment Config | python-dotenv          |

---

ETL Pipeline Design

### 1. Ingest
- Reads data from CSV files and cryptocurrency APIs (CoinPaprika & CoinGecko)  
- Converts raw data into structured Python dictionaries  

### 2. Transform
- Cleans missing values  
- Normalizes inconsistent fields  
- Prepares DB-ready schema  

### 3. Load
- Inserts processed data using SQLAlchemy ORM  
- Handles safe database transactions  
- Supports reprocessing of failed batches  

---

##  API Endpoints
| Method | Endpoint           | Description           |
|--------|------------------|----------------------|
| POST   | /api/v1/records   | Insert a new record  |
| GET    | /api/v1/records   | Fetch all records    |

---

##  Docker Support
The project includes:  
- `Dockerfile`  
- `docker-compose.yml`  

 Ensures environment consistency and easy deployment.

---

##  Key Engineering Principles
- Modular architecture  
- Clear separation of concerns  
- Environment-based configuration  
- Dependency injection  
- Clean CRUD abstraction  
- Testable design  
- Production-ready structure  

---

##  Testing
- Basic API tests implemented using Pytest  
- Validates: API availability, record insertion, data retrieval  

---

##  What This Demonstrates
- Real-world backend engineering workflow  
- ETL system design understanding  
- API + Database integration  
- Docker-based deployment readiness  
- Clean and maintainable system architecture  

---

##  Failure Handling & Recovery Strategy
**API-Level Safety:**  
- Database sessions managed using dependency injection  
- Input validation with Pydantic  
- Auto-generated API docs prevent malformed requests  

**ETL-Level Recovery:**  
- Each ETL stage isolated  
- Transformation failures do not corrupt raw data  
- Database commits are transactional  
- Failed batches can be safely reprocessed
  
  ## 📊 System Architecture Diagram (Textual)
             +----------------------+
           |     External Data     |
           |  (CSV / Crypto APIs)  |
           +-----------+----------+
                       |
                       ▼
                [ Ingest Layer ]
                       |
                       ▼
              [ Transform Layer ]
                       |
                       ▼
                [ Load Layer ]
                       |
                       ▼
                  [ Database ]
                       |
                       ▼
              [ FastAPI REST API ]
                       |
                       ▼
                    [ Client ]

---

## Future Improvements
- PostgreSQL / MySQL instead of SQLite  
- Redis-based job queue for ETL  
- Background processing using Celery / RQ  
- OpenTelemetry logging & monitoring  
- JWT authentication for API security  
- Retry mechanisms for failed ETL batches  
- Schema versioning & migration automation  
- Cloud deployment with CI/CD pipeline  

---

## Final Note
This project is built with **clarity, correctness, and maintainability** as primary goals, following Kasparro’s emphasis on **real engineering over shallow tasks**.
