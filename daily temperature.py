class Solution(object):
    def dailyTemperatures(self, temperatures):
      n = len(temperatures)
      ans = [0 for _ in range(n)]
      st = []
      for i in range(0, n):
          while (len(st)>0) and temperatures[i]> temperatures[st[len(st)-1]]:
              index = st[len(st)-1]
              st.pop()
              ans[index] = i-index
          st.append(i)
      return list(ans)
