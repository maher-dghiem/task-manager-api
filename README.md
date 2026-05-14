Project Overview

🔐 Authentication (JWT)
User registration

Login with access + refresh tokens

Token refresh endpoint

DRF defaults: JWTAuthentication + IsAuthenticated

👤 Accounts App
RegisterSerializer + RegisterView + LogoutView

/auth/register/, /auth/login/, /auth/refresh/, /auth/logout

📝 Tasks App
Task model fields:  
title, description, due_date, priority, status, owner

Features:

CRUD operations via TaskViewSet

Users see only their tasks

Admins see all tasks

Auto‑assign owner on create

🔒 Custom Permission
IsOwnerOrAdmin

Owners → full access

Admins → full access

Others → denied

🔍 Filtering, Search & Ordering
Search: title, description

Ordering: due_date, priority

Examples:

/tasks/?search=meeting

/tasks/?ordering=-due_date

📄 Pagination
Custom pagination class

Page size: 5 (max 20)

⚠️ Custom Exception Handling
Clean JSON responses for:

404

Permission denied

Validation errors

🌐 URL Structure
/auth/ → accounts

/tasks/ → tasks (DRF router)
