class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [ -count for count in counts.values()]
        heapq.heapify(heap)

        # the heap stores all the tasks that can be done
        # You only add it there if its ready and existing
        # q stores the tasks that can go in order because time increments by one everytime so each entry is in order of wait time when considering q = [cnt, ready_time]
        q = deque() 
        time = 0
        while heap or q:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                cnt = q.popleft()[0]
                heapq.heappush(heap,cnt)
                
            
                    
        return time
                