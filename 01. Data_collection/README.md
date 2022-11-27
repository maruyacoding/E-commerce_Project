# Data별 시각화 진행
- 정리한 노션 : https://www.notion.so/11-12-Data-547037c7174344de917ec14669e9e828

# Data별 column 설명

1. customers 
    - customer_id : Each order has a unique customer_id -> Key to the orders dataset (PK, Primary key)
    - customer_unique_id : unique identifier of a customer
    - customer_zip_code_prefix : first five digits of customer zip code
    - customer_city : customer city name
    - customer_state : customer state

2. geolocation
    - geolocation_zip_code_prefix : first 5 digits of zip code
    - geolocation_lat : latitude
    - geolocation_lng : longitude
    - geolocation_city : city name
    - geolocation_state : state

3. order_items
    - order_id : order unique identifier
    - order_item_id : sequential number identifying number of items included in the same order
    - product_id : product unique identifier
    - seller_id : seller unique identifier
    - shipping_limit_date : Shows the seller shipping limit date for handling the order over to the logistic partner
    - price : item price
    - freight_value : item freight value item (if an order has more than one item the freight value is splitted between items)
    
4. order_payments
    - order_id : unique identifier of an order
    - payment_sequential : a customer may pay an order with more than one payment method. If he does so, a sequence will be created to
    - payment_type : method of payment chosen by the customer
    - payment_installments : number of installments chosen by the customer
    - payment_value : transaction value

5. order_reviews
    - review_id : unique review identifier
    - order_id : unique order identifier
    - review_score : Note ranging from 1 to 5 given by the customer on a satisfaction survey
    - review_comment_title : Comment title from the review left by the customer, in Portuguese
    - review_comment_message : Comment message from the review left by the customer, in Portuguese
    - review_creation_date : Shows the data in which the satisfaction survey was sent to the customer
    - review_answer_timestamp : Shows satisfaction survey answer timestamp

6. orders
    - order_id : unique identifier of the order
    - customer_id : key to the customer dataset. Each order has a unique customer_id. (PK)
    - order_status : Reference to the order status (delivered, shipped, etc).
    - order_purchase_timestamp : Shows the purchase timestamp
    - order_approved_at : Show the payment approval timestamp
    - order_delivered_carrier_date : Shows the order posting timestamp. When it was handled to the logistic partner.
    - order_delivered_customer_date : Shows the actual order delivery date to the customer.
    - order_estimated_delivery_date : Shows the estimated delivery date that was informed to customer at the purchase moment.

7. products
    - product_id : unique product identifier
    - product_category_name : root category of product, in Portuguese.
    - product_name_lenght : number of characters extracted from the product name.
    - product_description_lenght : number of characters extracted from the product description.
    - product_photos_qty : number of product published photos
    - product_weight_g : product weight measured in grams.
    - product_length_cm : product length measured in centimeters.
    - product_height_cm : product height measured in centimeters.
    - product_width_cm : product width measured in centimeters.

8. sellers
    - seller_id : seller unique identifier
    - seller_zip_code_prefix : first 5 digits of seller zip code
    - seller_city : seller city name
    - seller_state : seller state

![image](https://user-images.githubusercontent.com/97514461/201132066-04e4168f-7ba6-45e4-be3d-58e540ffb0a0.png)
---
