public class Solution {
    public IList<string> GenerateParenthesis(int n) {
        List<string> res = new List<string>();
        Backtrack(res, "", 0, 0, n);
        return res;
    }

    private void Backtrack(List<string> res, string path, int openN, int closedN, int n) {
        if (openN == n && closedN == n) {
            res.Add(path);
            return;
        }

        if (openN < n) {
            Backtrack(res, path + "(", openN + 1, closedN, n);
        }

        if (closedN < openN) {
            Backtrack(res, path + ")", openN, closedN + 1, n);
        }
    }
}