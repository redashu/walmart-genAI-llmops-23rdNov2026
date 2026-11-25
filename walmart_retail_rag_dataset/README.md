# Retail Customer Support RAG Dataset

Purpose: Synthetic training knowledge base for a retail customer-support RAG demonstration.

IMPORTANT:
- These are fictional example policies and workflows.
- They are NOT Walmart's official policies and must not be presented as such.
- Replace the sample rules with approved company documents before any production use.
- The dataset intentionally includes clear eligibility limits and escalation guidance so the RAG assistant can practice grounded answers.

Documents:
1. order_tracking.md
2. return_policy.md
3. refund_policy.md
4. damaged_items.md
5. delivery_policy.md
6. payment_issues.md

Suggested ingestion:
- Load each Markdown file as a separate source document.
- Preserve document_id, category, title and version as metadata.
- Chunk by headings/sections where possible.
- Store source filename and section title with each chunk.
