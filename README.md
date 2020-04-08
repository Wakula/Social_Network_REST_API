# Social_Network_REST_API

## Usage
### Sensitive data
create '.env' file in api/ directory
```
DEBUG=on
DATABASE_URL=psql://postgres:password@localhost:5432/social_network_db
SECRET_KEY=tq6)l93)rvjz_)(x#$@st7*+tm(838fy)so5ig5^d^$3=ptn&0
ALLOWED_HOSTS=127.0.0.1,localhost
SIGNING_KEY=tq6)l93)rvjz_)(x#$@st7*+tm(838fy)so5ig5^d^$3=ptn&0
```
### API
Registration
```http
POST /api/accounts/
```
Sign in/Refresh
```http
POST /api/access-token/
POST /api/refresh-token/
```
Posts interaction
```http
POST /api/posts/
GET /api/posts/
GET /api/posts/<int:pk>/
```
Like/Unlike
```http
POST /api/posts/<int:pk>/like
DELETE /api/posts/<int:pk>/like
```
Like analytics
```http
GET /api/like-analytics/?date_from=2020-04-01&date_to=2020-04-08
```
User last activity
```http
GET /api/accounts/<int:pk>/last-activity/
```
