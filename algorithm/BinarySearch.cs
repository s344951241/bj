public class BinarySearch
{
    public static int search(int[] arr,int num,int start,int end)
    {
        if (start <= end)
        {
            int mid = (start + end) / 2;
            if (arr[mid] == num)
            {
                return mid;
            }
            else if (num < arr[mid])
            {
                return search(arr, num, start, mid);
            }
            else
            {
                return search(arr, num, mid + 1, end);
            }
        }
        else
        {
            return -1;
        }
    }
}