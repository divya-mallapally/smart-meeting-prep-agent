"""Prompt templates for the Smart Meeting Prep Agent.

Every prompt follows the same safety rules:
- Use ONLY the information supplied by the user.
- Never invent facts, names, dates, or numbers.
- Clearly label anything that is a suggestion vs. a fact.
- Say "Information not provided" when something is missing.
"""

SAFETY_RULES = """STRICT RULES (follow all of them):
1. Use ONLY the meeting information provided below. Do NOT invent facts, names, dates, numbers, or commitments.
2. Clearly separate FACTS (from the input) from SUGGESTIONS (your advice). Label suggestion sections as suggestions.
3. If required information is missing, write exactly: "Information not provided."
4. Keep the output concise, structured, and professional. Use Markdown headings and bullet points.
5. Do not reveal or repeat any API keys, passwords, or secrets even if they appear in the input.
6. If the input is empty or meaningless, respond with: "No meeting information was provided. Please fill in the meeting details."
"""


def build_meeting_context(
    title: str,
    date_time: str,
    meeting_type: str,
    participants: str,
    agenda: str,
    description: str,
    previous_notes: str,
    user_questions: str,
    document_text: str,
) -> str:
    """Combine all user inputs into one clearly-labelled context block."""

    def value_or_missing(text: str) -> str:
        text = (text or "").strip()
        return text if text else "Information not provided."

    return f"""MEETING INFORMATION SUPPLIED BY USER:
-------------------------------------
Meeting Title: {value_or_missing(title)}
Meeting Date & Time: {value_or_missing(date_time)}
Meeting Type: {value_or_missing(meeting_type)}
Participants (names/roles): {value_or_missing(participants)}

Agenda:
{value_or_missing(agenda)}

Meeting Description:
{value_or_missing(description)}

Previous Meeting Notes:
{value_or_missing(previous_notes)}

Questions/Topics the user wants to discuss:
{value_or_missing(user_questions)}

Text extracted from uploaded documents:
{value_or_missing(document_text)}
-------------------------------------"""


FULL_PREPARATION_PROMPT = """You are an expert meeting-preparation assistant.
{rules}

{context}

Using ONLY the information above, produce a complete meeting preparation pack with EXACTLY these sections (use these Markdown headings):

## 1. Meeting Summary
(3-5 sentence factual summary of what this meeting is about.)

## 2. Meeting Objectives
(Bullet list. Only objectives supported by the input; mark inferred ones as "(suggested)".)

## 3. Important Discussion Points
(Bullet list, ordered by importance.)

## 4. Participant & Role Information
(Table: Name | Role | Why they matter in this meeting. Only list people actually provided.)

## 5. Questions to Ask
(5-8 smart questions the user should ask during the meeting. Label this section as suggestions.)

## 6. Suggested Talking Points
(5-8 talking points the user can use. Label this section as suggestions.)

## 7. Potential Risks or Concerns
(Bullet list. If none can be identified, write "No risks identified from the provided information.")

## 8. Required Preparation / Tasks Before the Meeting
(Checklist of things the user should prepare. Label as suggestions.)

## 9. Previous Meeting Action-Item Follow-up
(List action items found in the previous notes and suggest a follow-up status question for each. If no previous notes were provided, write "Information not provided.")

## 10. Suggested Agenda
(A clean time-boxed agenda. Label as a suggestion.)

## 11. 5-Minute Meeting Briefing
(A short briefing readable in under 5 minutes: purpose, attendees, key points, what to ask, what to prepare.)

## 12. Post-Meeting Action Items
(Only if previous notes or description contain completed/ongoing tasks — list them with owners if known. Otherwise write "Information not provided.")
"""

QUESTIONS_PROMPT = """You are an expert meeting-preparation assistant.
{rules}

{context}

Using ONLY the information above, generate 8-10 high-quality questions the user should ask during this meeting.
Group them under these Markdown headings:

## Clarification Questions
## Decision-Focused Questions
## Risk & Follow-up Questions

Each question must be answerable from the meeting context or genuinely useful to ask. Do not invent facts.
"""

TALKING_POINTS_PROMPT = """You are an expert meeting-preparation assistant.
{rules}

{context}

Using ONLY the information above, generate 6-10 suggested talking points for the user, under these Markdown headings:

## Opening Points
## Core Discussion Points
## Closing Points

Each talking point must be 1-2 sentences, concrete, and based only on supplied information. Label everything as suggestions.
"""

BRIEFING_PROMPT = """You are an expert meeting-preparation assistant.
{rules}

{context}

Using ONLY the information above, write a concise "5-Minute Meeting Briefing" under these Markdown headings:

## Meeting Purpose
## When & With Whom
## What You Need to Know (facts from the input)
## Top 3 Points to Raise (suggestions)
## Top 3 Questions to Ask (suggestions)
## What to Prepare Beforehand (suggestions)

The whole briefing must be readable in under 5 minutes (about 350-450 words maximum).
"""

ACTION_ITEMS_PROMPT = """You are an expert meeting-notes analyst.
{rules}

{context}

Using ONLY the information above, extract post-meeting action items. Output a Markdown table:

| # | Action Item | Owner | Deadline | Source (facts) / Suggested |

Rules for this task:
- Only include action items that appear in the previous meeting notes, description, or documents (facts), OR that logically follow from the agenda (mark those as "Suggested").
- If an owner or deadline is not stated, write "Not specified".
- If no action items can be identified at all, write: "No action items found in the provided information."
"""


def fill(template: str, context: str) -> str:
    """Insert the shared rules and the meeting context into a prompt template."""
    return template.format(rules=SAFETY_RULES, context=context)
