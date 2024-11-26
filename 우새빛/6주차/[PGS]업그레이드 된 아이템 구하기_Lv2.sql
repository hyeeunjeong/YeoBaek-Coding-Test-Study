-- 코드를 작성해주세요
SELECT INF.ITEM_ID, INF.ITEM_NAME, INF.RARITY
FROM ITEM_INFO INF JOIN ITEM_TREE TRE ON INF.ITEM_ID = TRE.ITEM_ID
WHERE TRE.PARENT_ITEM_ID IN (SELECT ITEM_ID FROM ITEM_INFO WHERE RARITY = 'RARE') --부모가 RARE 단계 찾기
ORDER BY ITEM_ID DESC