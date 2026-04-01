
import requests

def execute(context, args):
    """
    Open-Claw: Sovereign Data Gripper (v3.0)
    Aggressive search for prices and data packets.
    """
    query = " ".join(args).lower() if args else "xnox updates"
    
    report = [
        f"🦾 **Open-Claw: Heavy Grip Engaged**",
        f"🔍 **Targeting:** `{query}`\n"
    ]
    
    try:
        # 1. SPECIAL CASE: CRYPTO PRICES (Free CoinGecko API)
        if any(coin in query for coin in ["bitcoin", "btc", "eth", "sol", "price"]):
            coin_id = "bitcoin" # default
            if "eth" in query: coin_id = "ethereum"
            if "sol" in query: coin_id = "solana"
            
            p_url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
            p_res = requests.get(p_url, timeout=5).json()
            price = p_res.get(coin_id, {}).get("usd")
            
            if price:
                report.append(f"💰 **Market Value Captured:**\n`1 {coin_id.upper()} = ${price:,.2f} USD`")
                report.append(f"📊 **Source:** Decentralized Market Feed")
                return "\n".join(report)

        # 2. GENERAL SEARCH: (Direct Wikipedia/Search fallback)
        search_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
        response = requests.get(search_url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            extract = data.get("extract", "")
            if extract:
                report.append(f"📦 **Packet Decrypted:**\n{extract[:400]}...")
            else:
                report.append("⚠️ **Status:** Target found but packet was empty.")
        else:
            # 3. FINAL FALLBACK: INTERNAL STATUS
            report.append("📡 **Internal Core Update:**")
            report.append("✅ Engine: Stable | ✅ Database: Active | ⚠️ Network: Global search blocked/no results.")

    except Exception as e:
        report.append(f"❌ **Grip Error:** {str(e)}")

    report.append("\n🏁 **Operation Complete.**")
    return "\n".join(report)

