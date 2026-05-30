# Product Brief: Marketing Health Snapshot

## Problem

Marketing teams repeatedly ask: **"How is our marketing performing across channels right now, and where should we focus?"**

Today, answering this requires manual work across multiple tools. Different people produce different answers, which creates delays, inconsistency, and dependency on specific team members.

## Primary User

**Internal Marketing Analyst**

The first version is designed for the internal analyst, not directly for clients. Analysts are the bottleneck today, and they already understand the business context behind each client account. Building for clients first would require permissions, client-specific customisation, polished UX, and explanation layers that are too heavy for v1.

## Proposed Solution

A lightweight internal dashboard called **Marketing Health Snapshot**.

The tool gives analysts a consistent view of:

- Spend by channel
- Conversions by channel
- CPA / CPL
- ROAS, where revenue data is available
- Week-over-week changes
- Channels that need attention

## Successful User Interaction

A user opens the tool, selects a client and date range, and can answer within minutes:

1. Are we improving or declining overall?
2. Which channel is performing best?
3. Which channel needs investigation?
4. What should be discussed in the next client/internal review?

## V1 Scope

### In scope

- Internal analyst-facing dashboard
- Daily refresh of channel-level metrics
- Client and date-range filters
- Core KPIs: spend, impressions, clicks, conversions, CPA/CPL, ROAS if available
- Simple rule-based alerts, for example:
  - CPA increased more than 20% week-over-week
  - Spend increased but conversions did not
  - Conversion rate dropped significantly
- Exportable summary for internal/client reporting

### Out of scope

- AI chatbot interface
- Predictive forecasting
- Automatic budget recommendations
- Campaign creation or editing
- Client-facing portal
- Multi-touch attribution modelling
- Real-time streaming dashboards

These are excluded because the first priority is to reduce manual reporting effort and create a trusted baseline. More advanced features should come only after validating that users trust and regularly use the core snapshot.

## Data Sources

The tool should fit around the existing workflow and tools. It should pull data from existing systems through APIs or scheduled exports.

Possible sources:

- Google Ads
- Meta Ads
- LinkedIn Ads
- GA4
- CRM or lead management system
- Revenue/order data, if available

## High-Level Architecture

```text
Marketing Platforms / Analytics Tools
        ↓
Scheduled Ingestion Jobs
        ↓
Raw Data Tables
        ↓
Transformation Layer
        ↓
Marketing KPI Tables
        ↓
Dashboard + Alert Summary
        ↓
Internal Marketing Analyst
```

## Trust Considerations

Users will trust the tool if it clearly shows:

- Last refresh timestamp
- Data source for each metric
- Definitions of KPIs
- Known data gaps
- Whether data is complete or partial
- Ability to compare against source tools during early rollout

## Future Enhancements

After v1 proves useful:

- Client-facing view
- AI-generated summaries
- Forecasting
- Budget allocation suggestions
- Automated anomaly detection
- Slack/email alerts
- Deeper attribution modelling

## Tradeoffs

I chose a dashboard-first approach instead of an AI assistant because the team first needs consistent, trusted metrics. An AI layer can be valuable later, but only after the underlying data definitions, refresh logic, and trust mechanisms are stable.
