                                Table "public.foodie_app_comment"
   Column   |           Type           | Collation | Nullable |             Default              
------------+--------------------------+-----------+----------+----------------------------------
 id         | bigint                   |           | not null | generated by default as identity
 content    | text                     |           | not null | 
 created_at | timestamp with time zone |           | not null | 
 author_id  | integer                  |           | not null | 
 recipe_id  | bigint                   |           | not null | 
 parent_id  | bigint                   |           |          | 
Indexes:
    "foodie_app_comment_pkey" PRIMARY KEY, btree (id)
    "foodie_app_comment_author_id_dacaf361" btree (author_id)
    "foodie_app_comment_parent_id_69b4a2ba" btree (parent_id)
    "foodie_app_comment_recipe_id_d092b42f" btree (recipe_id)
Foreign-key constraints:
    "foodie_app_comment_author_id_dacaf361_fk_auth_user_id" FOREIGN KEY (author_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED
    "foodie_app_comment_parent_id_69b4a2ba_fk_foodie_app_comment_id" FOREIGN KEY (parent_id) REFERENCES foodie_app_comment(id) DEFERRABLE INITIALLY DEFERRED
    "foodie_app_comment_recipe_id_d092b42f_fk_foodie_app_recipe_id" FOREIGN KEY (recipe_id) REFERENCES foodie_app_recipe(id) DEFERRABLE INITIALLY DEFERRED
Referenced by:
    TABLE "foodie_app_comment" CONSTRAINT "foodie_app_comment_parent_id_69b4a2ba_fk_foodie_app_comment_id" FOREIGN KEY (parent_id) REFERENCES foodie_app_comment(id) DEFERRABLE INITIALLY DEFERRED

