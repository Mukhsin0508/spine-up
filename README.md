# SpineUp

<a href="https://wakatime.com/badge/user/60731bfe-5801-4003-b6ab-b7db12ed73d0/project/3421f5b7-5631-4d5a-b61b-2a481e6e6c5a"><img src="https://wakatime.com/badge/user/60731bfe-5801-4003-b6ab-b7db12ed73d0/project/3421f5b7-5631-4d5a-b61b-2a481e6e6c5a.svg" alt="wakatime"></a>

## Overview

SpineUp is a comprehensive web platform built with Django that offers educational products/courses, job listings, team showcasing, and an AI-powered chatbot. The platform integrates with AmoCRM for customer relationship management.

## System Architecture

### Project Structure

```mermaid
graph TD
    A[SpineUp Project] --> B[src]
    B --> C[apps]
    B --> D[config]
    B --> E[media]
    B --> F[static]

    C --> G[amocrm]
    C --> H[base]
    C --> I[chatbot]
    C --> J[products]
    C --> K[vacancy]
    C --> L[web]

    D --> M[settings]
    D --> N[urls.py]
    D --> O[wsgi.py]

    E --> P[certificates]
    E --> Q[company_certificates]
    E --> R[post-images]
    E --> S[resumes]
    E --> T[staff_images]
```

### Data Flow

```mermaid
flowchart LR
    A[User] --> B[Web Interface]
    B --> C[Django Views]
    C --> D[Django Models]
    D --> E[Database]

    A --> F[Chatbot Interface]
    F --> G[Chatbot App]
    G --> H[RAG Model]
    H --> I[AI Response]
    I --> F

    J[Admin] --> K[Django Admin]
    K --> D

    L[Job Applicant] --> M[Vacancy Application]
    M --> N[Application Model]
    N --> E

    O[Client] --> P[CRM Integration]
    P --> Q[AmoCRM]
```

## Apps and Their Purposes

### 1. Base App
The foundation of the project, providing shared functionality:
- File management services for handling file uploads and deletions
- Signal handlers for automatic file cleanup
- Core utilities used across the platform

### 2. Chatbot App
An AI-powered conversation system:
- Custom user model for chat participants
- Conversation and message tracking
- RAG (Retrieval-Augmented Generation) model integration for context-aware responses
- API endpoints for chat interaction

### 3. Products App
Manages educational products/courses:
- Course details including title, description, duration, and number of sessions
- Image galleries for visual representation
- Session scheduling with day-of-week tracking
- Step-by-step session structure

### 4. Vacancy App
Job board functionality:
- Job posting with title, description, and salary range
- Job requirements listing
- Application submission and tracking
- Resume upload and validation

### 5. Web App
Main website content management:
- Staff profiles with images and positions
- Professional certificates for staff members
- Company certifications and credentials

### 6. AmoCRM App
Customer relationship management integration:
- Client data collection and storage
- Service request tracking
- Platform information
- Integration with AmoCRM external service

## Database Schema

```mermaid
erDiagram
    CustomSender ||--o{ Conversation : initiates
    Conversation ||--o{ Message : contains
    Message ||--|| RAGResponse : generates

    PostProduct ||--o{ TwoPictures : displays
    PostProduct ||--o{ TenPictures : displays
    PostProduct ||--o{ ClassDay : schedules
    PostProduct ||--o{ SessionStep : structures

    PostVacancy ||--o{ JobRequirement : requires
    PostVacancy ||--o{ Application : receives

    Staff ||--o{ Certificate : holds
    CompanyCertificate }o--|| Company : belongs-to

    ClientData }o--|| Service : requests
```

## Setup and Installation

### Prerequisites
- Python 3.x
- Docker (optional, for containerized deployment)
- PostgreSQL (or other database supported by Django)

### Environment Variables
Create a `.env` file in the project root with the following variables:
```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
INTERNAL_IPS=127.0.0.1
CORS_ALLOW_ALL_ORIGINS=True

# Database settings
DATABASE_URL=postgres://user:password@localhost:5432/spineup

# Email settings
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
EMAIL_HR_USER=hr@example.com

# Timezone settings
TIME_ZONE=UTC
USE_I18N=True
USE_TZ=True

# CSRF settings
CSRF_TRUSTED_ORIGINS=http://localhost:8000,https://yourdomain.com
```

### Local Development Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spineup.git
   cd spineup
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python src/manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python src/manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python src/manage.py runserver
   ```

### Docker Deployment
1. Build and start the containers:
   ```bash
   docker-compose up -d
   ```

2. Apply migrations:
   ```bash
   docker-compose exec web python src/manage.py migrate
   ```

3. Create a superuser:
   ```bash
   docker-compose exec web python src/manage.py createsuperuser
   ```

## Usage Examples

### Managing Products
1. Access the Django admin at `/admin`
2. Navigate to the Products section
3. Add a new product with title, description, and other details
4. Add session steps to structure the product's curriculum
5. Set class days for scheduling

### Using the Chatbot
1. Integrate the chatbot widget on your website
2. Initialize a conversation with a user
3. Messages are processed through the RAG model
4. AI-generated responses are returned to the user

### Posting Job Vacancies
1. Create a new vacancy with title, description, and salary range
2. Add specific job requirements
3. Monitor incoming applications through the admin interface

## Contributing
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
