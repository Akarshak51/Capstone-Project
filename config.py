# Configuration file for SupportHub AI
# Centralizes model selection and settings for all agents.

# API Configuration
GEMINI_API_KEY = "AIzaSyDqAthpwhYNsaGIHvLiy7t6lfOngTMsa2A"

# Model Configuration
PRIMARY_MODEL = "gemini-2.0-flash-exp"  # Fast model for most tasks
ANALYTICS_MODEL = "gemini-1.5-pro"  # More powerful for analytics

# Vertex AI Configuration (if using GCP)
PROJECT_ID = "your-gcp-project-id"  # Replace with your GCP project
LOCATION = "us-central1"

# Agent Settings
MAX_LOOP_ITERATIONS = 3  # For response generation loop
TICKET_BATCH_SIZE = 10  # For batch processing

# Tool Timeouts (seconds)
CRM_TIMEOUT = 5
TICKET_QUERY_TIMEOUT = 5
KB_SEARCH_TIMEOUT = 3

# Notification Settings
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
EMAIL_FROM = "supporthub-ai@example.com"
ESCALATION_EMAIL = "support-team@example.com"

# SLA Thresholds (hours)
SLA_FIRST_RESPONSE = 1  # First response within 1 hour
SLA_RESOLUTION_LOW = 24
SLA_RESOLUTION_MEDIUM = 8
SLA_RESOLUTION_HIGH = 4
SLA_RESOLUTION_CRITICAL = 1

# Sentiment Thresholds
SENTIMENT_ALERT_THRESHOLD = -0.7  # Alert if sentiment very negative
SENTIMENT_ESCALATION_THRESHOLD = -0.9  # Auto-escalate if extremely negative

# Memory Bank Settings
MEMORY_BANK_TOP_K = 5  # Number of relevant memories to retrieve
MEMORY_SAVE_MIN_EVENTS = 2  # Minimum events before saving to memory

# Analytics Settings
ANALYTICS_WINDOW_DAYS = 7  # Analyze last 7 days of tickets
TREND_MIN_OCCURRENCES = 3  # Minimum occurrences to flag as trend
