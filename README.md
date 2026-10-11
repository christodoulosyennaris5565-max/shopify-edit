# Helia Web — studio site

Source for the heliaweb.com homepage (Shopify theme "Helia Web — studio site").

- `theme/templates/index.liquid` — page shell (title, meta, fonts)
- `theme/sections/heliaweb.liquid` — renders the snippets below
- `theme/snippets/hw-styles-1.liquid`, `hw-styles-2.liquid` — CSS
- `theme/snippets/hw-part-a.liquid` — nav, hero, pricing, sample work (Crumbs, Solomou Woodworking)
- `theme/snippets/hw-part-b.liquid` — industries, how it works, FAQ
- `theme/snippets/hw-part-c.liquid` — contact details, contact form, footer

Prices: static websites from €650 one-time, apps from €1,000. Shops/payments/booking: by quote.

## Quote builder and client tracker

- `/pages/get-a-quote` (`templates/page.quote.liquid`, `snippets/qt-*.liquid`): step-by-step quote with live price and production time. Prices and questions live at the top of `snippets/qt-script.liquid`. After sending, the client picks "Move forward" (pay €50 deposit) or "Request a call".
- `/pages/my-project` (`templates/page.project.liquid`, `snippets/pj-body.liquid`): clients sign in with their email (one-time code) and see their stage.
- Stages come from the customer metafield **Project stage** (Shopify admin > Customers > customer > Metafields): Quote submitted, Call requested, Awaiting deposit, In production, Website live. Paying the "Website deposit" product moves a client to In production automatically.
- Other customer metafields shown to the client: Project type, Final quote, Message to client.
