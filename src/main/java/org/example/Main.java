package org.example;
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.*;
import java.io.File;
import java.util.Scanner;


// All services demonstrated in this assignment are owned by Amazon web service [1].


public class Main {
    public static S3Client createS3Client(Region region) {
        return S3Client.builder().region(region).credentialsProvider(DefaultCredentialsProvider.create()).build(); //[2]
    }
    public static void createBucket(S3Client s3Client, String bucketName) {
        CreateBucketRequest createBucketRequest = CreateBucketRequest.builder().bucket(bucketName).build(); //[3]
        s3Client.createBucket(createBucketRequest);
        System.out.println("bucket created");
    }
    public static void uploadFile(S3Client s3Client, String bucketName, String filePath, String key) {
        File file = new File(filePath);
        PutObjectRequest putObjectRequest = PutObjectRequest.builder().bucket(bucketName).key(key).build(); //[4]
        s3Client.putObject(putObjectRequest, RequestBody.fromFile(file));
        System.out.println("file uploaded");
    }

    public static void deleteFile(S3Client s3Client, String bucketName, String key){
        DeleteObjectRequest request= DeleteObjectRequest.builder().bucket(bucketName).key(key).build(); //[5]
        s3Client.deleteObject(request);
        System.out.println("file dleted");
    }
    public static void deleteBucket(S3Client s3Client, String bucketName){
        DeleteBucketRequest deleteBucketRequest=DeleteBucketRequest.builder().bucket(bucketName).build(); //[6]
        s3Client.deleteBucket(deleteBucketRequest);
        System.out.println("bucket deleted");
    }


    public static void main(String[] args) {
        String bucketName = "b00934548-bucket";
        Region region = Region.US_EAST_1;
        S3Client s3Client = createS3Client(region); //[2]
        Scanner scanner = new Scanner(System.in);
        int operation = scanner.nextInt();
        switch (operation) {
            case 1:
                try {
                    createBucket(s3Client, bucketName);
                    break;
                }
                catch (S3Exception e) {
                    System.err.println(e.awsErrorDetails().errorMessage());
                    System.exit(1);
                }

            case 2:
                try {
                    uploadFile(s3Client, bucketName, "C:\\Users\\AVuser\\Desktop\\serverless 5410\\S3 assignment\\S3_Assignment\\index.html", "index.html");
                    break;
                }
                catch (S3Exception e) {
                    System.err.println(e.awsErrorDetails().errorMessage());
                    System.exit(1);
                }

            case 3:
                try {
                    deleteFile(s3Client, bucketName, "index.html");
                    break;
                }
                catch (S3Exception e) {
                    System.err.println(e.awsErrorDetails().errorMessage());
                    System.exit(1);
                }
            case 4:
                try {
                    deleteBucket(s3Client, bucketName);
                    break;

                }
                catch (S3Exception e) {
                    System.err.println(e.awsErrorDetails().errorMessage());
                    System.exit(1);
                }

            default:
                System.err.println("Invalid operation number.");
                System.exit(1);
                break;
        }
    }
}

//References:
//[1] Amazon Web Services, Inc., "Amazon Web Services (AWS) - Cloud Computing Services," Amazon Web Services, Inc., 2023. [Online]. Available: https://aws.amazon.com/. [Accessed 1 June 2023].
//[2] Amazon Web Services, Inc., "Interface S3Client," Amazon Web Services, Inc., 2023. [Online]. Available: https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3Client.html. [Accessed 3 June 2023].
//[3] Amazon Web Services, Inc., "Class CreateBucketRequest," Amazon Web Services, Inc., 2023. [Online]. Available: https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/model/CreateBucketRequest.html. [Accessed 03 June 2023].
//[4] Amazon Web Services, Inc., "Class PutObjectRequest," Amazon Web Services, Inc., 2023. [Online]. Available: https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/model/PutObjectRequest.html. [Accessed 03 June 2023].
//[5] N. H. Minh, "AWS Java SDK S3 Delete Objects Examples," CodeJava.net, 2023. [Online]. Available: https://www.codejava.net/aws/delete-s3-objects-examples. [Accessed 03 June 2023].
//[6] N. H. Minh, "AWS Java SDK S3 Delete Buckets Examples," CodeJava.net, 2023. [Online]. Available: https://www.codejava.net/aws/delete-buckets-examples. [Accessed 03 June 2023].
