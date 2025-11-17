import Image from "next/image";

export const UserCard = () => {
  return (
    <div className="flex items-center justify-center">
      <Image
        className="rounded-full mr-2"
        alt="123"
        src="/image.png"
        width={50}
        height={50}
      />
      <div className="flex flex-col flex-1 w-40 mr-4">
        <div className="font-bold text-[14px]">thang.pham</div>
        <div className="text-gray-500 text-[12px]">Gợi ý cho bạn</div>
      </div>
      <button className="text-[#708DFF] font-semibold text-[12px]">
        Theo dõi
      </button>
    </div>
  );
};
