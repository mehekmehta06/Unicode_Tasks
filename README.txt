Django Backend Projects
1)Pokedex App: This app is used for finding pokemon and its various characteristics. I have used an external API to get the data and stored it in the database/models. 
2)Blog Website: The Backend comprises of CRUD operations on blog. It also contains permission to only logged in users to perform delete and update operations. I have implemented registration and login.
3)Investment Portfolio: The project uses Django rest framework. The main aim of the project is to have a space for keeping the investment details at one place.
Features included:
•User Registration sign up
     -New user creation (Anyone can create an account )
•Creating a portfolio
     -Portfolio contains 
        1.	Full Name
        2.	Contact no
        3.	Email
        4.	Stock investment details: name of company ,no.of stocks , year in which stocks were bought
        5.	MF investment details: MF amount,start date
•Current market updates
     -Use api to get current stock and unit prices : using GET whenever signed in user whats to view.(permission only to members)
•Transaction log
     -Only for users having investment in MF 
     -Keep track of next monthly Sip pyments
•Reminder about monthly sip payments
     -Will use transaction log date to send mail reminder on the registered email(Permission only to members)
•Resources
     -Use GET operation for accessing various online resources(added links in this model and only those will be accessible)
•Membership
     -Payment getaway 
     -Membership required for availing some features
•Return on investment and portfolio valuation
     -Make model in which ROI and valuation will be calculated for each user 
     -GET permission only to members













