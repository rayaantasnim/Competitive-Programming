from collections import defaultdict

# ১. ইনপুট নেওয়া
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# ২. প্রতিটি কাজের জন্য মানুষের বুঝানোর সময়গুলো গ্রুপ করা
job_to_costs = defaultdict(list)
for i in range(n):
    job = A[i]
    cost = B[i]
    job_to_costs[job].append(cost)

# ৩. কোন মানুষগুলোকে আমরা সরাতে পারি (removable_costs) তা বের করা
removable_costs = []
chosen_jobs_count = len(job_to_costs) # কতটি কাজ অলরেডি অন্তত ১ জন বেছে নিয়েছে

for job, costs in job_to_costs.items():
    # খরচগুলোকে ছোট থেকে বড় ক্রমে সর্ট করি
    costs.sort()
    
    # সবচেয়ে বড় খরচটি (costs[-1]) ওই কাজের জন্য রেখে দেব, একে সরানো যাবে না।
    # বাকি ছোট খরচগুলো (costs[:-1]) আমরা সরাতে পারি, তাই removable_costs-এ রাখব।
    for c in costs[:-1]:
        removable_costs.append(c)

# ৪. কতটি কাজ একদম খালি আছে (কেউ বেছে নেয়নি) তা হিসাব করা
needed = k - chosen_jobs_count

# ৫. অতিরিক্ত মানুষদের মধ্য থেকে সবচেয়ে কম সময়ের মানুষদের বেছে নেওয়া
removable_costs.sort() # ছোট থেকে বড় ক্রমে সর্ট

# প্রথম থেকে 'needed' সংখ্যক মানুষের সময়ের যোগফলই হলো সর্বনিম্ন সময়
ans = sum(removable_costs[:needed])

# ৬. ফলাফল প্রিন্ট করা
print(ans)
