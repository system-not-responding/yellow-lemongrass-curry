# clear terminal each time
import os
os.system('cls')

# inputs for questions
print("Welcome to the TradeGate Program.\n".upper())

tick_value = float(input("What's the dollar amount per tick?\n$"))

tick_risk = int(input("How many ticks are you risking?\n"))

tick_reward = int(input("How many ticks is the reward?\n"))

contract_number = int(input("How many contracts?\n"))

portfolio_balance = float(input("What's your portfolio balance OR max allowable loss?\n$"))

# maths

# calculating risk
currency_risk = "{:.2f}".format(tick_value * contract_number * tick_risk)
currency_risk = float(currency_risk)                                                                # converts to float
currency_risk = float("{:.2f}".format(currency_risk))                                               # formats float to have 2 decimal places (not working currently)
risk_one_more_contract = float((contract_number + 1) * tick_value * tick_risk)                      # calculates risking one more contract
risk_one_less_contract = float("{:.2}".format((contract_number - 1) * tick_value * tick_risk))
risk_portfolio_balance_percent = float((currency_risk / portfolio_balance))                         # calculates risk as a percent to the portfolio balance
suggested_risk_percent = (portfolio_balance / 100)
risk_one_more_contract_percent = (risk_one_more_contract - currency_risk) / portfolio_balance


# calculating reward
currency_reward = "{:.2f}".format(tick_value * contract_number * tick_reward)
currency_reward = float(currency_reward)
reward_portfolio_balance_percent = float((currency_reward / portfolio_balance) / 100)               

reward_one_more_contract = float("{:.2}".format((contract_number + 1) * tick_value * tick_reward))  # calculates reward with one more contract
reward_one_less_contract = float("{:.2}".format((contract_number - 1) * tick_value * tick_reward))

suggested_reward_percent = (portfolio_balance * .03)

# creating risk: reward ratio
risk_ratio = (tick_reward / tick_risk)

# 1st box responses. -1 risk and reward not working. Showing $ amount of 0
print("\nBasic Stats") # title for box 1
print("----------------------------------------------")

risk_response = ("{:.2f}".format(float(currency_risk)))                                              # formats risk to have 2 decimal points (not working)
risk_response = print(f"\nYour risk is: ${(currency_risk)}")                                         # prints risk response
reward_response = print(f"Your reward is: ${currency_reward}\n")                                     # prints reward response

risk_ratio_response = print(f"Your risk-to-reward ratio is: {risk_ratio}\n")                         # prints risk to reward response


risk_portfolio_balance_percent_response = print(f"Portfolio risk: {round(risk_portfolio_balance_percent * 100, 2)}%")
reward_portfolio_balance_percent_response = print(f"Portfolio reward: {round(risk_portfolio_balance_percent * 100, 2) * risk_ratio}%\n") 

suggested_risk_percent_response = print(f"Suggested portfolio risk percent: 10% (${portfolio_balance * .1}) - 13% (${portfolio_balance * .13})")
suggested_reward_percent_response = print(f"Suggested portfolio reward percent: 30% (${portfolio_balance * .3}) - 39% (${portfolio_balance * .39})\n")

print("\n")

print("Can you place a trade?")
print("----------------------------------------------")


# i want to add in the flowchart below

if risk_portfolio_balance_percent <= (13 / 100):
    print(f"Your risk meets the treshold: {round(risk_portfolio_balance_percent * 100, 2)}% / 13%")
    if risk_ratio >= 2:
        print(f"Your risk-to-reward meets the minimum requirement: {risk_ratio} / 2\n")
        price_action = input("Is price action Trending or Chopping?\n").lower()
        if price_action == "trending":
            pa_trending_yes = input("Are you buying with the trend? Yes or no?\n").lower()
            if pa_trending_yes == "yes":
                pa_trending_buy_delta = input("Is delta confirming a long bias?\n").lower()
                if pa_trending_buy_delta == "yes":
                    print("Delta confirms your long bias. Place the trade on a pullback.")  
                else:
                    print("Delta does not confirm your bias. You cannot place a trade.")
            else:
                shorting_with_trend = input("Are you shorting with the trend?\n").lower()
                if shorting_with_trend == 'yes':
                    short_delta_confirmation = input("Does delta confirm this short bias?\n").lower()
                    if short_delta_confirmation == 'yes':
                        print("You can short on a pullback.")
                    else:
                        print("Delta does not confirm this short bias. You cannot place a trade.")
                else:
                    print("This is countertrend. You cannot place a trade.")
                    
# below is chopping if elses
        else:
            pa_chopping = input("Are you buying the bottom?\n")
            if pa_chopping == "yes":
                pa_chopping_failed_breakout = input("Is there a failed breakout?\n")
                if pa_chopping_failed_breakout == "yes":
                    pa_chopping_delta_confirmed = input("Does delta confirm a long bias?\n")
                    if pa_chopping_delta_confirmed == 'yes':
                        print("You can place a trade at the body of the candlestick")
                    else:
                        print("Delta does not confirm this long bias. You cannot place a trade.")
                else:
                    pa_chopping_failed_breakout = input("Does delta confirm a long bias?\n")
                    if pa_chopping_failed_breakout == "yes":
                        print("Place trade below longest wick.")
                    else:
                        print("Delta does not confirm a long bias. You cannot place a trade.")
            else:
                pa_chopping_failed_breakout = input("Are you shorting the top?\n")
                if pa_chopping_failed_breakout == "yes":
                    pa_chopping_failed_breakout = input("Is there a failed breakout?\n")
                    if pa_chopping_failed_breakout == "yes":
                        pa_chopping_delta_confirmed = input("Does delta confirm a short bias?\n")
                        if pa_chopping_delta_confirmed == "yes":
                            print("Place trade at the body of the candlestick")
                        else:
                            print("Delta does not confirm this short bias. You cannot place a trade.")
                    else:
                        pa_chopping_failed_breakout = input("Does delta confirm a short bias?\n")
                        if pa_chopping_failed_breakout == "yes":
                            print("Place trade just passed longest wick.")
                        else:
                            print("Delta does not confirm a short bias. You cannot place a trade.")

                else:
                    print("You're neither going long nor short. There's no trade to take.")
    else:
        print(f"Your risk-to-reward does not meet the minimum requirement: {risk_ratio} / 2\n")    
else:
    print(f"Your risk exceeds threshold: {round(risk_portfolio_balance_percent * 100, 2)}%/ 13%. You cannot place a trade")




print("\n")