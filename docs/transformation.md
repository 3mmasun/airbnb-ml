# columns in valid parquet files

```
airbnb_df.dtypes.value_counts()
```

| type    | occurance |
| ------- | --------- |
| float64 | 38        |
| object  | 32        |
| int32   | 2         |

## objects

`cat_df = airbnb_df.select_dtypes(include=['object']).copy()`

### dropped

| Column                 | Reason                                |
| ---------------------- | ------------------------------------- |
| rowId                  | not used                              |
| id                     | not used                              |
| host_location          | duplicate with longitude and altitude |
| host_neighbourhood     | too granular                          |
| street                 | too granular                          |
| neighbourhood          | too granular                          |
| neighbourhood_cleansed | too granular                          |
| market                 | 99.9% same value "Barcelona"          |
| license                | too granular                          |

### transformed

| Column                       | Transformation                |
| ---------------------------- | ----------------------------- |
| host_since                   |
| host_response_time           |
| host_is_superhost            | encode_boolean_to_float       |
| host_verifications           |
| host_has_profile_pic         | encode_boolean_to_float       |
| host_identity_verified       | encode_boolean_to_float       |
| neighbourhood_group_cleansed | encode_category_dic           |
| zipcode                      | drop_rows_occurs_less_than(7) |
| property_type                | encode_category_dic           |
| room_type                    | encode_category_dic           |
| bed_type                     | encode_category_dic           |
| amenities                    |
| calendar_updated             |
| first_review                 |
| last_review                  |
| cancellation_policy          | encode_category_dic           |

## float64 and int32

`numeric_df = airbnb_df.select_dtypes(include=['float64', 'int32']).copy()`

### dropped

| Column | Reason |
| ------ | ------ |
| name   | ...    |

### transformed

| Column                                       | Transformation |
| -------------------------------------------- | -------------- |
| host_response_rate                           |
| host_listings_count                          |
| host_total_listings_count                    |
| latitude                                     |
| longitude                                    |
| accommodates                                 |
| bathrooms                                    |
| bedrooms                                     |
| beds                                         |
| price                                        |
| security_deposit                             |
| cleaning_fee                                 |
| guests_included                              |
| extra_people                                 |
| minimum_nights                               |
| maximum_nights                               |
| minimum_minimum_nights                       |
| maximum_minimum_nights                       |
| minimum_maximum_nights                       |
| maximum_maximum_nights                       |
| minimum_nights_avg_ntm                       |
| maximum_nights_avg_ntm                       |
| availability_30                              |
| availability_60                              |
| availability_90                              |
| availability_365                             |
| number_of_reviews                            |
| number_of_reviews_ltm                        |
| review_scores_rating                         |
| review_scores_accuracy                       |
| review_scores_cleanliness                    |
| review_scores_checkin                        |
| review_scores_communication                  |
| review_scores_location                       |
| review_scores_value                          |
| calculated_host_listings_count               |
| calculated_host_listings_count_entire_homes  |
| calculated_host_listings_count_private_rooms |
| calculated_host_listings_count_shared_rooms  |
| reviews_per_month                            |
