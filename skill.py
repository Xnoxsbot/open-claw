
import requests

def execute(context, args):
    """
    Open-Claw: Sovereign Data Gripper (v3.4)
    'Clean Iron Grip' - Precision Price Retrieval.
    """
    query = " ".join(args).lower() if args else "bitcoin"
    
    report = [
        f"🦾 **Open-Claw: Iron Grip Engaged**",
        f"🔍 **Targeting:** `{query}`\n"
    ]
    
    try:
        # 1. THE IRON GRIP (CoinDesk Public API)
        if any(coin in query for coin in ["bitcoin", "btc", "price"]):
            url = "https://api.coindesk.com/v1/bpi/currentprice.json"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                price = data['bpi']['USD']['rate_float']
                
                report.append(f"💰 **Live Market Data Captured:**")
                report.append(f"`1 BTC = ${price:,.2f} USD`")
                report.append(f"✅ **Source:** CoinDesk Feed")
                return "\n".join(report)

        # 2. INTEL GRIP (DuckDuckGo API)
        search_url = f"https://api.duckduckgo.com/?q={query}&format=json"
        res = requests.get(search_url, timeout=10)
        if res.status_code == 200:
            abs_text = res.json().get("AbstractText", "")
            if abs_text:
                report.append(f"📦 **Packet Decrypted:**\n{abs_text[:500]}...")
                return "\n".join(report)

        report.append("⚠️ **Status:** No clear signal for this target.")

    except Exception as e:
        report.append(f"❌ **Grip Error:** {str(e)}")

    return "\n".join(report)

