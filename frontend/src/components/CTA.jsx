import SignInModal from "./SignInModal";
export default function CTA() {
  return (
    <section className="my-16 px-4 md:px-0 flex flex-col items-center justify-center gap-8">
      <h1 className="text-3xl font-black">Stay Ahead of the Game</h1>
      <p className="max-w-[40ch] text-center">Embrace the future of talent verification and give your company the edge it needs to thrive in today’s competitive job market. Join Talent Verify Online today!</p>
      <SignInModal title="Get Started Now" />
    </section>
  );
}