tot_ean = 0
count = 0
while True:
    s_ean = input("Enter a number: ", )
    if s_ean == 'done':
        print('Total:', tot_ean,' Count:', count,' Average:', tot_ean/count)
        break
    try:
        f_ean = int(s_ean)
    except:
        print("bad #")
        continue
    count = count + 1
    tot_ean = f_ean + tot_ean

# tot_ean = 0
# s_ean = None
# count = 0
# avg = 0
#
# while True:
#     s_ean = input("Enter a number: ", )
#
#     if s_ean == 'done':
#         print('Total: ', tot_ean)
#         print('Count: ', count)
#         print('Average: ', avg)
#         break
#
#     for total in s_ean:
#         try:
#             f_ean = int(s_ean)
#         except:
#             print("bad #")
#             continue
#         count = count + 1
#         tot_ean = f_ean + tot_ean
#         avg = tot_ean / count
