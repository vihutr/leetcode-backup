# @leet start
class AccountAssociation:
    accs = {}
    names = {}
        
    def find(self, acc):
        # using accs dict in some ways as linked list
        # every acc wants to both associate with a universal parent set
        # as well as be able to be referenced by the prev/point to the next item
        # recursive loop to find root of chain of emails(id/key)
        # email: email: ... email: name: id of account
        # should follow above structure due to names being the first processed
        # when looping through account data
        f = accs.get(acc, acc)
        # .get usage yields associated value in the chain
        # or the acc if no associated value aka its the end of the chain
        if f != acc:
            # if we find an associated value, continue
            accs.

    def merge_sets(self, email1, email2):
        # union
        # associate email with a prior email in chain of references



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # create ids for each user, then store set of emails and + name for each id
        # have to be able to look up id and find an email in the set
        merged_accounts = {}
        names = {}
        latest_id = 0
        for a in accounts:
            name = a[0]
            emails = a[1:]
            # check merged_accounts for a matching email
            matching_acc = None
            copy_emails = emails
            for e in emails:
                for id in merged_accounts:
                    # search through all accounts for email
                    if e in merged_accounts[id]:
                        # if email found, track the id as the matching acc
                        # also remove the matching email from the emails to append
                        matching_acc = id
                        copy_emails.remove(e)
            if matching_acc is not None:
                for e in copy_emails:
                    if e not in merged_accounts[matching_acc]:
                        merged_accounts[matching_acc].append(e)
            else:
                merged_accounts[latest_id] = []
                for e in emails:
                    if e not in merged_accounts[latest_id]:
                        merged_accounts[latest_id].append(e)
                names[latest_id] = name
                latest_id += 1
        result = []
        for i in range(latest_id):
            entry = [names[i]]
            for a in sorted(merged_accounts[i]):
                entry.append(a)
            result.append(entry)
        return result
            
# @leet end
