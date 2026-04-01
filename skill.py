
import requests
import json

def execute(context, args):
    """
    Open-Claw: Sovereign Data Gripper (v2.0)
    Grips real-time data using free web scrapers.
    """
    query = " ".join(args) if args else "Xnox AI updates"
    
    # 1. Engage the Grip UI
    report = [
        f"🦾 **Open-Claw: Data Grip Engaged**",
        f"🔍 **Targeting:** `{query}`\n"
    ]
    
    try:
        # 2. THE GRAB (Using a Free DuckDuckGo API proxy for real data)
        # This doesn't require a paid API key!
        search_url = f"https://api.duckduckgo.com/?q={query}&format=json"
        response = requests.get(search_url, timeout=10)
        data = response.json()
        
        # 3. ANALYZE THE PACKET
        abstract = data.get("AbstractText", "")
        related = data.get("RelatedTopics", [])
        
        if abstract:
            report.append(f"📦 **Captured Data:**\n{abstract}")
        elif related:
            # Grab the first 3 related snippets if no main abstract exists
            snippets = []
            for item in related[:3]:
                if 'Text' in item:
                    snippets.append(f"• {item['Text']}")
            
            if snippets:
                report.append("📦 **Captured Data Snippets:**")
                report.extend(snippets)
            else:
                report.append("⚠️ **Status:** Target found but packet was empty/encrypted.")
        else:
            # Fallback to internal core status if the web search is empty
            report.append("📡 **Internal Core Update:**")
            report.append("✅ Engine: Stable | ✅ Database: Active | ⚠️ Network: Search yielded no direct results.")

    except Exception as e:
        report.append(f"❌ **Grip Error:** Failed to bypass security. {str(e)}")

    report.append("\n🏁 **Operation Complete.** Data delivered to Xnox.")
    return "\n".join(report)
