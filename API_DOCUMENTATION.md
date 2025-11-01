# Geeks Andijan Courses API - Frontend Documentation

Complete API documentation for frontend developers integrating with the Geeks Andijan Courses API.

## 📋 Table of Contents

- [Base URL](#base-url)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [Courses](#courses)
  - [Leads](#leads)
- [Error Handling](#error-handling)
- [Code Examples](#code-examples)
- [TypeScript Types](#typescript-types)

---

## 🌐 Base URL

**Development:**
```
http://localhost:8000/api
```

**Production:**
```
https://yourapp.pythonanywhere.com/api
```

Replace `yourapp` with your actual PythonAnywhere username.

---

## 🔐 Authentication

### Public Endpoints (No Authentication Required)
- `GET /api/courses/` - List all courses
- `GET /api/courses/<id>/` - Get single course
- `POST /api/leads/` - Submit a lead

### Admin-Only Endpoints (Staff Authentication Required)
- `GET /api/leads/admin/` - List all leads (requires Django admin/staff user)

For admin endpoints, you need to authenticate using Django's session authentication or token authentication. The user must have `is_staff=True` in Django admin.

**Session Authentication (Cookie-based):**
```javascript
// Django session authentication happens automatically when logged in via admin panel
// No additional headers needed if using cookies
```

**Token Authentication (if configured):**
```javascript
headers: {
  'Authorization': 'Token <your-token>'
}
```

---

## 📚 Endpoints

### Courses

#### 1. List All Courses

**Endpoint:** `GET /api/courses/`

**Description:** Retrieve a list of all courses with their details.

**Access:** Public (no authentication required)

**Request:**
```http
GET /api/courses/
```

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "title": "Python Fundamentals",
    "description": "Learn Python programming from scratch. This comprehensive course covers...",
    "for_who": "beginners",
    "details": {
      "pluses": ["mentor", "project", "team", "certificate"],
      "inthis_course": [
        {
          "question": "What will I learn?",
          "answer": "Python basics, data structures, functions, and object-oriented programming"
        },
        {
          "question": "How long is the course?",
          "answer": "3 months with 2 sessions per week"
        }
      ]
    },
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
  },
  {
    "id": 2,
    "title": "Advanced Web Development",
    "description": "Master React, Next.js, and modern web development...",
    "for_who": "professionals",
    "details": {
      "pluses": ["mentor", "project", "team", "certificate"],
      "inthis_course": [
        {
          "question": "Prerequisites?",
          "answer": "Basic knowledge of HTML, CSS, and JavaScript"
        }
      ]
    },
    "created_at": "2024-01-20T14:00:00Z",
    "updated_at": "2024-01-20T14:00:00Z"
  }
]
```

**Possible Values for `for_who`:**
- `"beginners"` - For beginners
- `"students"` - For students
- `"professionals"` - For professionals

---

#### 2. Get Single Course

**Endpoint:** `GET /api/courses/<id>/`

**Description:** Retrieve detailed information about a specific course by ID.

**Access:** Public (no authentication required)

**Parameters:**
- `id` (integer, required) - The unique identifier of the course

**Request:**
```http
GET /api/courses/1/
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "title": "Python Fundamentals",
  "description": "Learn Python programming from scratch...",
  "for_who": "beginners",
  "details": {
    "pluses": ["mentor", "project", "team", "certificate"],
    "inthis_course": [
      {
        "question": "What will I learn?",
        "answer": "Python basics, data structures, functions, and OOP"
      }
    ]
  },
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

**Error Response:** `404 Not Found`
```json
{
  "detail": "Not found."
}
```

---

### Leads

#### 3. Submit Course Lead

**Endpoint:** `POST /api/leads/`

**Description:** Submit a new course lead (inquiry). This endpoint is publicly accessible and does not require authentication.

**Access:** Public (no authentication required)

**Request Headers:**
```http
Content-Type: application/json
```

**Request Body:**
```json
{
  "fullname": "John Doe",
  "age": 25,
  "phone": "+998901234567"
}
```

**Field Requirements:**
- `fullname` (string, required) - Full name of the lead (max 100 characters)
- `age` (integer, required) - Age of the lead (must be between 1 and 150)
- `phone` (string, required) - Phone number (max 20 characters, cannot be empty)

**Request:**
```http
POST /api/leads/
Content-Type: application/json

{
  "fullname": "John Doe",
  "age": 25,
  "phone": "+998901234567"
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "fullname": "John Doe",
  "age": 25,
  "phone": "+998901234567",
  "created_at": "2024-01-25T12:00:00Z"
}
```

**Error Response:** `400 Bad Request`
```json
{
  "fullname": ["This field is required."],
  "age": ["Age must be between 1 and 150."],
  "phone": ["Phone number cannot be empty."]
}
```

---

#### 4. List All Leads (Admin Only)

**Endpoint:** `GET /api/leads/admin/`

**Description:** Retrieve a list of all course leads. **This endpoint is restricted to admin users only.**

**Access:** Admin only (requires `is_staff=True`)

**Request Headers:**
```http
Authorization: Token <your-admin-token>
```
OR (if using session authentication)
```http
Cookie: sessionid=<session-id>
```

**Request:**
```http
GET /api/leads/admin/
```

**Response (Admin):** `200 OK`
```json
[
  {
    "id": 1,
    "fullname": "John Doe",
    "age": 25,
    "phone": "+998901234567",
    "created_at": "2024-01-25T12:00:00Z"
  },
  {
    "id": 2,
    "fullname": "Jane Smith",
    "age": 22,
    "phone": "+998901234568",
    "created_at": "2024-01-26T10:15:00Z"
  }
]
```

**Error Response (Non-Admin):** `403 Forbidden`
```json
{
  "detail": "You do not have permission to perform this action."
}
```

**Error Response (Unauthenticated):** `403 Forbidden`
```json
{
  "detail": "Authentication credentials were not provided."
}
```

---

## ⚠️ Error Handling

### HTTP Status Codes

| Status Code | Meaning | When It Occurs |
|------------|---------|----------------|
| `200 OK` | Success | Request completed successfully |
| `201 Created` | Success | Resource created successfully |
| `400 Bad Request` | Client Error | Invalid request data or validation failed |
| `403 Forbidden` | Client Error | Insufficient permissions (admin-only endpoint) |
| `404 Not Found` | Client Error | Resource not found |
| `500 Internal Server Error` | Server Error | Server-side error |

### Error Response Format

All error responses follow this format:

**Single Field Error:**
```json
{
  "field_name": ["Error message"]
}
```

**Multiple Field Errors:**
```json
{
  "field1": ["Error message 1"],
  "field2": ["Error message 2"]
}
```

**Generic Error:**
```json
{
  "detail": "Error message"
}
```

### Common Validation Errors

**Age Validation:**
- Age must be a positive integer
- Age must be between 1 and 150

**Phone Validation:**
- Phone number cannot be empty
- Phone number must be a string (max 20 characters)

**Fullname Validation:**
- Fullname is required
- Fullname must be a string (max 100 characters)

---

## 💻 Code Examples

### JavaScript (Fetch API)

#### Get All Courses
```javascript
async function getAllCourses() {
  try {
    const response = await fetch('https://yourapp.pythonanywhere.com/api/courses/');
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const courses = await response.json();
    console.log('Courses:', courses);
    return courses;
  } catch (error) {
    console.error('Error fetching courses:', error);
    throw error;
  }
}
```

#### Get Single Course
```javascript
async function getCourseById(courseId) {
  try {
    const response = await fetch(
      `https://yourapp.pythonanywhere.com/api/courses/${courseId}/`
    );
    
    if (!response.ok) {
      if (response.status === 404) {
        throw new Error('Course not found');
      }
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const course = await response.json();
    return course;
  } catch (error) {
    console.error('Error fetching course:', error);
    throw error;
  }
}
```

#### Submit Course Lead
```javascript
async function submitLead(leadData) {
  try {
    const response = await fetch('https://yourapp.pythonanywhere.com/api/leads/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        fullname: leadData.fullname,
        age: leadData.age,
        phone: leadData.phone,
      }),
    });
    
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(JSON.stringify(errorData));
    }
    
    const createdLead = await response.json();
    console.log('Lead submitted successfully:', createdLead);
    return createdLead;
  } catch (error) {
    console.error('Error submitting lead:', error);
    throw error;
  }
}

// Usage
submitLead({
  fullname: 'John Doe',
  age: 25,
  phone: '+998901234567',
});
```

#### Get All Leads (Admin Only)
```javascript
async function getAllLeads(adminToken) {
  try {
    const response = await fetch('https://yourapp.pythonanywhere.com/api/leads/admin/', {
      method: 'GET',
      headers: {
        'Authorization': `Token ${adminToken}`,
        'Content-Type': 'application/json',
      },
    });
    
    if (!response.ok) {
      if (response.status === 403) {
        throw new Error('Access forbidden. Admin privileges required.');
      }
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const leads = await response.json();
    return leads;
  } catch (error) {
    console.error('Error fetching leads:', error);
    throw error;
  }
}
```

---

### React (Next.js) Examples

#### Custom Hook for Courses
```typescript
// hooks/useCourses.ts
import { useState, useEffect } from 'react';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'https://yourapp.pythonanywhere.com/api';

export interface Course {
  id: number;
  title: string;
  description: string;
  for_who: 'beginners' | 'students' | 'professionals';
  details: {
    pluses: string[];
    inthis_course: Array<{
      question: string;
      answer: string;
    }>;
  };
  created_at: string;
  updated_at: string;
}

export function useCourses() {
  const [courses, setCourses] = useState<Course[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchCourses() {
      try {
        setLoading(true);
        const response = await fetch(`${API_BASE_URL}/courses/`);
        
        if (!response.ok) {
          throw new Error('Failed to fetch courses');
        }
        
        const data = await response.json();
        setCourses(data);
        setError(null);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'An error occurred');
      } finally {
        setLoading(false);
      }
    }

    fetchCourses();
  }, []);

  return { courses, loading, error };
}
```

#### Course Lead Form Component
```typescript
// components/CourseLeadForm.tsx
'use client';

import { useState } from 'react';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'https://yourapp.pythonanywhere.com/api';

interface LeadFormData {
  fullname: string;
  age: number;
  phone: string;
}

export default function CourseLeadForm() {
  const [formData, setFormData] = useState<LeadFormData>({
    fullname: '',
    age: 0,
    phone: '',
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setSuccess(false);

    try {
      const response = await fetch(`${API_BASE_URL}/leads/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(JSON.stringify(errorData));
      }

      const result = await response.json();
      console.log('Lead submitted:', result);
      setSuccess(true);
      setFormData({ fullname: '', age: 0, phone: '' });
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to submit lead');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label htmlFor="fullname">Full Name</label>
        <input
          id="fullname"
          type="text"
          value={formData.fullname}
          onChange={(e) => setFormData({ ...formData, fullname: e.target.value })}
          required
          maxLength={100}
        />
      </div>

      <div>
        <label htmlFor="age">Age</label>
        <input
          id="age"
          type="number"
          min={1}
          max={150}
          value={formData.age}
          onChange={(e) => setFormData({ ...formData, age: parseInt(e.target.value) })}
          required
        />
      </div>

      <div>
        <label htmlFor="phone">Phone</label>
        <input
          id="phone"
          type="tel"
          value={formData.phone}
          onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
          required
          maxLength={20}
        />
      </div>

      {error && <div className="error">{error}</div>}
      {success && <div className="success">Lead submitted successfully!</div>}

      <button type="submit" disabled={loading}>
        {loading ? 'Submitting...' : 'Submit'}
      </button>
    </form>
  );
}
```

---

## 📘 TypeScript Types

### Course Types
```typescript
export type TargetAudience = 'beginners' | 'students' | 'professionals';

export interface CourseDetail {
  pluses: string[];
  inthis_course: Array<{
    question: string;
    answer: string;
  }>;
}

export interface Course {
  id: number;
  title: string;
  description: string;
  for_who: TargetAudience;
  details: CourseDetail | null;
  created_at: string;
  updated_at: string;
}
```

### Lead Types
```typescript
export interface CourseLead {
  id: number;
  fullname: string;
  age: number;
  phone: string;
  created_at: string;
}

export interface CourseLeadCreateRequest {
  fullname: string;
  age: number;
  phone: string;
}
```

### Error Types
```typescript
export interface ValidationError {
  [field: string]: string[];
}

export interface APIError {
  detail?: string;
  [key: string]: string[] | string | undefined;
}
```

---

## 🔧 Environment Variables

Create a `.env.local` file in your Next.js project:

```env
NEXT_PUBLIC_API_URL=https://yourapp.pythonanywhere.com/api
```

Then use it in your code:
```typescript
const API_URL = process.env.NEXT_PUBLIC_API_URL;
```

---

## 📝 Best Practices

1. **Always handle errors**: Wrap API calls in try-catch blocks
2. **Show loading states**: Provide user feedback during API calls
3. **Validate on client-side**: Validate data before sending to API (but don't rely solely on client-side validation)
4. **Use TypeScript**: Define types for all API responses
5. **Handle network errors**: Account for network failures and timeouts
6. **Respect rate limits**: Don't make excessive API calls
7. **Store API URL in environment variables**: Never hardcode URLs

---

## 🆘 Support

For API issues or questions:
1. Check error responses for validation messages
2. Verify CORS settings if experiencing CORS errors
3. Ensure admin endpoints use proper authentication
4. Contact the backend team for API-related issues

---

## 📄 License

This API is proprietary software for Geeks Andijan.

---

**Last Updated:** 2024-01-25

