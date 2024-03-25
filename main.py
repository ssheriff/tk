import library_modules as my


def main():
    profile, region = my.get_cmd_args()
    print(profile, region)

    boto_session = my.get_session(profile, region)
    ec2_client = my.get_client(boto_session, "ec2")

    testObj = my.tkwin()
    testObj.mainloop()


if __name__ == "__main__":
    main()
